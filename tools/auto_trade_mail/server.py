# -*- coding: utf-8 -*-
"""
Lightweight REST API & Web Server for Auto Trade Mail
基于 Python 标准库实现的纯净高效本地 Web 服务
"""
import json
import urllib.parse
import threading
import os
import mimetypes
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from typing import Dict, Any

from config import WEB_HOST, WEB_PORT, BASE_DIR
from db import init_db, get_connection, get_dashboard_stats
from mailer import (
    CampaignRunner, execute_campaign, test_smtp_connection, 
    render_template, get_eligible_leads_for_step
)
from warmup import WarmupRunner, execute_warmup_task, get_mailboxes_warmup_status
from importer import import_leads_from_rows, parse_csv_content
from oauth_outlook import build_authorization_url, exchange_code_for_token

STATIC_DIR = BASE_DIR / "static"
PENDING_OAUTH = {}

class TradeMailHandler(BaseHTTPRequestHandler):
    def send_json(self, data: Any, status: int = 200):
        body = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, message: str, status: int = 400):
        self.send_json({"error": message, "success": False}, status=status)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def read_json_body(self) -> Dict[str, Any]:
        content_length = int(self.headers.get("Content-Length", 0))
        if content_length == 0:
            return {}
        raw = self.rfile.read(content_length).decode("utf-8")
        try:
            return json.loads(raw)
        except Exception:
            return {}

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        # 1. 静态网页与静态资源 (图片、资产等)
        if path == "/" or path == "/index.html":
            file_path = STATIC_DIR / "index.html"
            if file_path.exists():
                with open(file_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            else:
                self.send_error(404, "Static index.html not found")
                return

        elif path.startswith("/static/"):
            rel_path = path[len("/static/"):].replace("/", os.sep)
            file_path = STATIC_DIR / rel_path
            if file_path.exists() and file_path.is_file():
                import mimetypes
                content_type, _ = mimetypes.guess_type(str(file_path))
                if not content_type:
                    content_type = "application/octet-stream"
                with open(file_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header("Content-Type", content_type)
                self.send_header("Content-Length", str(len(content)))
                self.send_header("Cache-Control", "public, max-age=86400")
                self.end_headers()
                self.wfile.write(content)
                return
            else:
                self.send_error(404, f"File not found: {path}")
                return

        # 2. API 路由
        if path == "/api/dashboard":
            stats = get_dashboard_stats()
            self.send_json({"success": True, "data": stats})
            return

        elif path == "/api/leads":
            conn = get_connection()
            cur = conn.cursor()
            status_filter = query.get("status", [None])[0]
            search = query.get("search", [None])[0]

            sql = "SELECT * FROM leads WHERE 1=1"
            params = []
            if status_filter:
                sql += " AND status = ?"
                params.append(status_filter)
            if search:
                sql += " AND (email LIKE ? OR company LIKE ? OR first_name LIKE ?)"
                kw = f"%{search}%"
                params.extend([kw, kw, kw])
            
            sql += " ORDER BY id DESC"
            cur.execute(sql, params)
            leads = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json({"success": True, "data": leads})
            return

        elif path == "/api/mailboxes":
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT id, email, sender_name, smtp_host, smtp_port, ssl_mode, username, daily_limit, sent_today, is_active, notes, auth_type FROM mailboxes ORDER BY id ASC")
            mailboxes = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json({"success": True, "data": mailboxes})
            return

        elif path == "/api/sequences":
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM sequences ORDER BY step_number ASC")
            seqs = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json({"success": True, "data": seqs})
            return

        elif path == "/api/campaign/status":
            runner = CampaignRunner.get_instance()
            self.send_json({"success": True, "data": runner.current_job})
            return

        elif path == "/api/warmup/status":
            runner = WarmupRunner.get_instance()
            self.send_json({"success": True, "data": runner.current_job})
            return

        elif path == "/api/warmup/mailboxes":
            boxes = get_mailboxes_warmup_status()
            self.send_json({"success": True, "data": boxes})
            return

        elif path == "/api/campaign/eligible":
            step = int(query.get("step", [1])[0])
            leads = get_eligible_leads_for_step(step)
            self.send_json({"success": True, "step": step, "count": len(leads), "leads": leads})
            return

        elif path == "/api/logs":
            conn = get_connection()
            cur = conn.cursor()
            limit = int(query.get("limit", [50])[0])
            status_filter = query.get("status", [None])[0]
            if status_filter and status_filter != "all":
                cur.execute("SELECT * FROM send_logs WHERE status = ? ORDER BY id DESC LIMIT ?", (status_filter, limit))
            else:
                cur.execute("SELECT * FROM send_logs ORDER BY id DESC LIMIT ?", (limit,))
            logs = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json({"success": True, "data": logs})
            return

        elif path == "/api/suppression":
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM suppression_list ORDER BY id DESC")
            items = [dict(r) for r in cur.fetchall()]
            conn.close()
            self.send_json({"success": True, "data": items})
            return

        elif path == "/api/auth/outlook/callback":
            code = query.get("code", [None])[0]
            error = query.get("error_description", [None])[0]
            if error:
                html = f"<html><body style='font-family:sans-serif;padding:40px;text-align:center;'><h2 style='color:#e11d48;'>微软授权失败</h2><p>{error}</p></body></html>"
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
                return

            if not code or "client_id" not in PENDING_OAUTH:
                html = "<html><body style='font-family:sans-serif;padding:40px;text-align:center;'><h2>缺少授权码或已过期</h2><p>请重新在发信工具中发起绑定。</p></body></html>"
                self.send_response(400)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
                return

            try:
                redirect_uri = f"http://localhost:{WEB_PORT}/api/auth/outlook/callback"
                tokens = exchange_code_for_token(
                    PENDING_OAUTH["client_id"],
                    PENDING_OAUTH["client_secret"],
                    redirect_uri,
                    code
                )
                access_tok = tokens.get("access_token", "")
                refresh_tok = tokens.get("refresh_token", "")
                exp_in = int(tokens.get("expires_in", 3600))
                import time
                exp_at = int(time.time() + exp_in)

                conn = get_connection()
                cur = conn.cursor()
                cur.execute("""
                INSERT INTO mailboxes (
                    email, sender_name, smtp_host, smtp_port, ssl_mode, username, password, daily_limit, notes,
                    auth_type, client_id, client_secret, refresh_token, access_token, token_expires_at
                ) VALUES (?, ?, 'smtp.office365.com', 587, 'starttls', ?, '', ?, ?, 'oauth2', ?, ?, ?, ?, ?)
                """, (
                    PENDING_OAUTH["email"],
                    PENDING_OAUTH["sender_name"],
                    PENDING_OAUTH["email"],
                    int(PENDING_OAUTH.get("daily_limit", 25)),
                    "Microsoft OAuth 2.0 (XOAUTH2)",
                    PENDING_OAUTH["client_id"],
                    PENDING_OAUTH["client_secret"],
                    refresh_tok,
                    access_tok,
                    exp_at
                ))
                conn.commit()
                conn.close()

                html = f"""
                <html>
                <body style='font-family: Arial, sans-serif; padding: 50px; text-align: center; background: #f8fafc;'>
                    <div style='max-width: 480px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);'>
                        <h2 style='color: #0284c7; margin-bottom: 10px;'>🎉 微软 Outlook 授权成功！</h2>
                        <p style='color: #475569; font-size: 14px;'>发件箱 <b>{PENDING_OAUTH['email']}</b> 已成功绑定到本地发信系统，并已启用 XOAUTH2 安全认证。</p>
                        <p style='color: #94a3b8; font-size: 12px; margin-top: 20px;'>您可以关闭此窗口，回到发信控制台刷新查看。</p>
                    </div>
                    <script>
                        setTimeout(() => {{ if (window.opener) {{ window.opener.location.reload(); window.close(); }} }}, 2000);
                    </script>
                </body>
                </html>
                """
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
            except Exception as e:
                html = f"<html><body style='font-family:sans-serif;padding:40px;text-align:center;'><h2 style='color:#e11d48;'>置换 Token 失败</h2><p>{str(e)}</p></body></html>"
                self.send_response(500)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(html.encode("utf-8"))
            return

        elif path == "/api/preview":
            step_num = int(query.get("step", [1])[0])
            lead_id = query.get("lead_id", [None])[0]
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM sequences WHERE step_number = ?", (step_num,))
            seq = cur.fetchone()
            if not seq:
                conn.close()
                self.send_error_json("Sequence not found", 404)
                return

            if lead_id:
                cur.execute("SELECT * FROM leads WHERE id = ?", (lead_id,))
                lead_row = cur.fetchone()
            else:
                cur.execute("SELECT * FROM leads ORDER BY id ASC LIMIT 1")
                lead_row = cur.fetchone()

            lead = dict(lead_row) if lead_row else {
                "first_name": "Megan",
                "company": "Northstar Boutique",
                "country": "United States",
                "title": "Lead Buyer",
                "custom_note": "Noticed your new store display in Seattle."
            }

            cur.execute("SELECT * FROM mailboxes WHERE is_active = 1 LIMIT 1")
            mbox_row = cur.fetchone()
            mbox = dict(mbox_row) if mbox_row else {
                "sender_name": "Bob (Encore Technical Sales)",
                "email": "bob@encore-lighting.com"
            }
            conn.close()

            subject = render_template(seq["subject"], lead, mbox)
            body = render_template(seq["body_template"], lead, mbox)

            self.send_json({
                "success": True,
                "step": step_num,
                "subject": subject,
                "body": body,
                "lead": lead,
                "mailbox": mbox
            })
            return

        elif path == "/api/encore/showcase":
            from encore_showcase_data import ENCORE_SEQUENCES, ENCORE_LEADS
            self.send_json({
                "success": True,
                "data": {
                    "sequences": ENCORE_SEQUENCES,
                    "leads": ENCORE_LEADS
                }
            })
            return

        elif path == "/api/encore/preview_rich":
            lead_idx = int(query.get("lead_index", [0])[0])
            step_num = int(query.get("step", [1])[0])
            from encore_showcase_data import ENCORE_SEQUENCES, ENCORE_LEADS
            if lead_idx >= len(ENCORE_LEADS):
                lead_idx = 0
            lead = ENCORE_LEADS[lead_idx]
            
            target_seq = next((s for s in ENCORE_SEQUENCES if s["step_number"] == step_num), ENCORE_SEQUENCES[0])
            
            subject = target_seq["subject"].format(
                first_name=lead["first_name"],
                company=lead["company"],
                country=lead["country"],
                recommended_product=lead["recommended_product"],
                subject_step1=lead["subject_step1"]
            )
            body = target_seq["body_template"].format(
                first_name=lead["first_name"],
                company=lead["company"],
                country=lead["country"],
                recommended_product=lead["recommended_product"],
                pain_point_opener=lead["pain_point_opener"],
                product_bullets=lead["product_bullets"],
                subject_step1=lead["subject_step1"]
            )

            # 匹配对应的高清产品图片 URL
            prod = str(lead.get("recommended_product", "")).upper()
            img_url = ""
            if "DELLA" in prod:
                img_url = "/static/assets/products/della.jpg"
            elif "48V" in prod or "MAGNETIC" in prod:
                img_url = "/static/assets/products/magnetic.jpg"
            elif "GALAXY" in prod:
                img_url = "/static/assets/products/galaxy.jpg"
            elif "VEGA" in prod:
                img_url = "/static/assets/products/vega.jpg"
            elif "MOVIA" in prod:
                img_url = "/static/assets/products/movia.jpg"
            
            self.send_json({
                "success": True,
                "data": {
                    "lead": lead,
                    "step_number": step_num,
                    "subject": subject,
                    "body": body,
                    "product_image": img_url,
                    "case_badge": "NIKE 连锁工程专供 (10+州 6,000+套定制灯具交付)"
                }
            })
            return

        self.send_error_json("Not Found", 404)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        body = self.read_json_body()

        if path == "/api/leads":
            email = body.get("email", "").strip()
            if not email:
                self.send_error_json("Email is required")
                return
            conn = get_connection()
            cur = conn.cursor()
            try:
                cur.execute("""
                INSERT INTO leads (email, first_name, company, title, country, category, custom_note)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    email,
                    body.get("first_name", ""),
                    body.get("company", ""),
                    body.get("title", ""),
                    body.get("country", ""),
                    body.get("category", "General"),
                    body.get("custom_note", "")
                ))
                conn.commit()
                conn.close()
                self.send_json({"success": True, "message": "Lead created successfully"})
            except Exception as e:
                conn.close()
                self.send_error_json(f"Failed to create lead: {str(e)}")
            return

        elif path == "/api/leads/import-csv":
            csv_text = body.get("csv_text", "")
            if not csv_text:
                self.send_error_json("No CSV content provided")
                return
            try:
                rows = parse_csv_content(csv_text)
                res = import_leads_from_rows(rows)
                self.send_json({"success": True, "data": res})
            except Exception as e:
                self.send_error_json(f"Import failed: {str(e)}")
            return

        elif path == "/api/leads/status":
            lead_id = body.get("id")
            new_status = body.get("status")
            if not lead_id or not new_status:
                self.send_error_json("id and status are required")
                return
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("UPDATE leads SET status = ? WHERE id = ?", (new_status, lead_id))
            
            # 如果标记为退订，同时写入黑名单表
            if new_status == "unsubscribed":
                cur.execute("SELECT email FROM leads WHERE id = ?", (lead_id,))
                row = cur.fetchone()
                if row:
                    cur.execute("INSERT OR IGNORE INTO suppression_list (email, reason) VALUES (?, 'Marked unsubscribed')", (row[0],))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Status updated"})
            return

        elif path == "/api/mailboxes":
            req_fields = ["email", "sender_name", "smtp_host", "smtp_port", "username", "password"]
            for f in req_fields:
                if not body.get(f):
                    self.send_error_json(f"Field {f} is required")
                    return
            conn = get_connection()
            cur = conn.cursor()
            cleaned_pwd = str(body["password"]).strip().replace(" ", "")
            try:
                cur.execute("""
                INSERT INTO mailboxes (email, sender_name, smtp_host, smtp_port, ssl_mode, username, password, daily_limit, notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    body["email"].strip(),
                    body["sender_name"].strip(),
                    body["smtp_host"].strip(),
                    int(body["smtp_port"]),
                    body.get("ssl_mode", "starttls"),
                    body["username"].strip(),
                    cleaned_pwd,
                    int(body.get("daily_limit", 25)),
                    body.get("notes", "")
                ))
                conn.commit()
                conn.close()
                self.send_json({"success": True, "message": "Mailbox added successfully"})
            except Exception as e:
                conn.close()
                self.send_error_json(f"Failed to add mailbox: {str(e)}")
            return

        elif path == "/api/mailboxes/update":
            mbox_id = body.get("id")
            if not mbox_id:
                self.send_error_json("Mailbox ID is required")
                return
            conn = get_connection()
            cur = conn.cursor()
            try:
                sender_name = body.get("sender_name", "").strip()
                smtp_host = body.get("smtp_host", "").strip()
                smtp_port = int(body.get("smtp_port", 587))
                ssl_mode = body.get("ssl_mode", "starttls")
                username = body.get("username", "").strip()
                daily_limit = int(body.get("daily_limit", 25))
                is_active = 1 if body.get("is_active", True) else 0
                new_pwd = str(body.get("password", "")).strip().replace(" ", "")

                if new_pwd:
                    cur.execute("""
                    UPDATE mailboxes
                    SET sender_name = ?, smtp_host = ?, smtp_port = ?, ssl_mode = ?, username = ?, password = ?, daily_limit = ?, is_active = ?
                    WHERE id = ?
                    """, (sender_name, smtp_host, smtp_port, ssl_mode, username, new_pwd, daily_limit, is_active, mbox_id))
                else:
                    cur.execute("""
                    UPDATE mailboxes
                    SET sender_name = ?, smtp_host = ?, smtp_port = ?, ssl_mode = ?, username = ?, daily_limit = ?, is_active = ?
                    WHERE id = ?
                    """, (sender_name, smtp_host, smtp_port, ssl_mode, username, daily_limit, is_active, mbox_id))
                conn.commit()
                conn.close()
                self.send_json({"success": True, "message": "Mailbox updated successfully"})
            except Exception as e:
                conn.close()
                self.send_error_json(f"Failed to update mailbox: {str(e)}")
            return

        elif path == "/api/mailboxes/test-by-id":
            mbox_id = body.get("id")
            if not mbox_id:
                self.send_error_json("Mailbox ID is required")
                return
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("SELECT * FROM mailboxes WHERE id = ?", (mbox_id,))
            row = cur.fetchone()
            conn.close()
            if not row:
                self.send_error_json("Mailbox not found")
                return
            mbox_dict = dict(row)
            ok, msg = test_smtp_connection(mbox_dict)
            self.send_json({"success": ok, "message": msg})
            return

        elif path == "/api/mailboxes/test":
            if "password" in body:
                body["password"] = str(body["password"]).strip().replace(" ", "")
            print(f"[DEBUG_TEST] Testing mailbox: host={body.get('smtp_host')}, port={body.get('smtp_port')}, ssl_mode={body.get('ssl_mode')}, user={body.get('username') or body.get('email')}")
            ok, msg = test_smtp_connection(body)
            print(f"[DEBUG_TEST] Result: ok={ok}, msg={msg}")
            self.send_json({"success": ok, "message": msg})
            return

        elif path == "/api/sequences/update":
            seq_id = body.get("id")
            subject = body.get("subject")
            body_template = body.get("body_template")
            delay_days = body.get("delay_days")
            if not seq_id:
                self.send_error_json("Sequence id is required")
                return
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("""
            UPDATE sequences 
            SET subject = COALESCE(?, subject),
                body_template = COALESCE(?, body_template),
                delay_days = COALESCE(?, delay_days)
            WHERE id = ?
            """, (subject, body_template, delay_days, seq_id))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Sequence template updated"})
            return

        elif path == "/api/campaign/start":
            runner = CampaignRunner.get_instance()
            if runner.is_running:
                self.send_error_json("A campaign is already running!")
                return
            
            step = int(body.get("step_number", 1))
            dry_run = bool(body.get("dry_run", True))
            lead_ids = body.get("lead_ids", None)

            # 在后台独立线程中执行发信，不卡死 Web 服务
            t = threading.Thread(target=execute_campaign, args=(step, dry_run, lead_ids), daemon=True)
            t.start()
            self.send_json({"success": True, "message": f"Campaign started for Step {step} (Dry-Run: {dry_run})"})
            return

        elif path == "/api/campaign/stop":
            runner = CampaignRunner.get_instance()
            runner.stop()
            self.send_json({"success": True, "message": "Stop request submitted"})
            return

        elif path == "/api/warmup/start":
            runner = WarmupRunner.get_instance()
            if runner.is_running:
                self.send_error_json("预热任务已在运行中，请勿重复启动！")
                return
            
            target_emails = body.get("target_emails", [])
            if not target_emails or not isinstance(target_emails, list):
                self.send_error_json("请提供至少一个接收预热的邮箱")
                return
            
            selected_mailbox_ids = body.get("selected_mailbox_ids", None)
            mode = body.get("mode", "smart") # "smart" or "force"
            target_count = int(body.get("target_count", 2))
            min_delay = int(body.get("min_delay", 25))
            max_delay = int(body.get("max_delay", 45))
            custom_topics = body.get("custom_topics", None)

            t = threading.Thread(
                target=execute_warmup_task,
                args=(target_emails, selected_mailbox_ids, mode, target_count, min_delay, max_delay, custom_topics),
                daemon=True
            )
            t.start()
            self.send_json({"success": True, "message": "预热养号任务已启动"})
            return

        elif path == "/api/warmup/stop":
            runner = WarmupRunner.get_instance()
            runner.stop()
            self.send_json({"success": True, "message": "已提交停止预热请求"})
            return

        elif path == "/api/encore/import_to_leads":
            # 将精选的 Encore 真实买家一键导入到自动化发信线索库
            from encore_showcase_data import ENCORE_LEADS
            conn = get_connection()
            cur = conn.cursor()
            imported_cnt = 0
            for l in ENCORE_LEADS:
                custom_note = f"项目背景: {l['project_reference']} | 推荐单品: {l['recommended_product']} | 首封切入: {l['pain_point_opener']}"
                try:
                    cur.execute("""
                    INSERT INTO leads (email, first_name, company, title, country, category, custom_note, status, current_step)
                    VALUES (?, ?, ?, ?, ?, ?, ?, 'active', 0)
                    ON CONFLICT(email) DO UPDATE SET
                        first_name = excluded.first_name,
                        company = excluded.company,
                        title = excluded.title,
                        country = excluded.country,
                        category = excluded.category,
                        custom_note = excluded.custom_note
                    """, (
                        l["email"],
                        l["first_name"],
                        l["company"],
                        l["title"],
                        l["country"],
                        l["category"],
                        custom_note
                    ))
                    imported_cnt += 1
                except Exception as e:
                    pass
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": f"成功将 {imported_cnt} 位精选买家线索导入系统客户库！", "count": imported_cnt})
            return

        elif path == "/api/encore/launch_mailmaster":
            # 一键调用本地网易邮箱大师 / 邮件客户端
            to_email = body.get("email", "Moissar@pxls.ae")
            subject = body.get("subject", "")
            body_text = body.get("body", "")
            try:
                import os
                params = urllib.parse.urlencode({'subject': subject, 'body': body_text[:1200]}, quote_via=urllib.parse.quote)
                url = f"mailto:{to_email}?{params}"
                try:
                    os.startfile(url)
                except Exception:
                    pass
                self.send_json({"success": True, "message": f"网易邮箱已准备就绪，收件人: {to_email}"})
            except Exception as e:
                self.send_json({"success": True, "message": f"邮件指令已生成: {to_email}"})
            return

        elif path == "/api/suppression":
            email = body.get("email", "").strip()
            reason = body.get("reason", "Manual addition")
            if not email:
                self.send_error_json("Email is required")
                return
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("INSERT OR IGNORE INTO suppression_list (email, reason) VALUES (?, ?)", (email, reason))
            # 标记 leads 状态为 unsubscribed
            cur.execute("UPDATE leads SET status = 'unsubscribed' WHERE lower(email) = lower(?)", (email,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": f"{email} added to suppression list"})
            return

        self.send_error_json("Not Found", 404)

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        if path.startswith("/api/leads/"):
            lead_id = path.split("/")[-1]
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM leads WHERE id = ?", (lead_id,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Lead deleted"})
            return

        elif path.startswith("/api/mailboxes/"):
            mbox_id = path.split("/")[-1]
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM mailboxes WHERE id = ?", (mbox_id,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Mailbox deleted"})
            return

        elif path.startswith("/api/suppression/"):
            sup_id = path.split("/")[-1]
            conn = get_connection()
            cur = conn.cursor()
            cur.execute("DELETE FROM suppression_list WHERE id = ?", (sup_id,))
            conn.commit()
            conn.close()
            self.send_json({"success": True, "message": "Removed from suppression list"})
            return

        self.send_error_json("Not Found", 404)

def run_server():
    init_db()
    server_address = (WEB_HOST, WEB_PORT)
    httpd = ThreadingHTTPServer(server_address, TradeMailHandler)
    print(f"================================================================")
    print(f" Auto Trade Mail - 自动化外贸开发信工作站")
    print(f" Web 控制台地址: http://{WEB_HOST}:{WEB_PORT}")
    print(f" 状态: 运行中 (按 Ctrl+C 退出)")
    print(f"================================================================")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
