# -*- coding: utf-8 -*-
"""
Core Mailer & Outreach Sequence Engine
严格遵循 marketing/skills/cold-outreach 规范的外贸发信引擎
"""
import smtplib
import ssl
import time
import random
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, make_msgid
from typing import Dict, Any, List, Optional, Tuple

from config import DEFAULT_SAFETY_CONFIG
from db import get_connection
from oauth_outlook import generate_xoauth2_string, refresh_access_token

def get_token_for_mailbox(mailbox: Dict[str, Any]) -> Tuple[str, str]:
    """确保获取有效的 Access Token (自动续期)"""
    access_token = mailbox.get("access_token", "")
    token_expires_at = mailbox.get("token_expires_at", 0)
    client_id = mailbox.get("client_id", "")
    client_secret = mailbox.get("client_secret", "")
    refresh_tok = mailbox.get("refresh_token", "")

    if (not access_token or time.time() >= token_expires_at - 60) and refresh_tok and client_id:
        try:
            access_token, expires_in = refresh_access_token(client_id, client_secret, refresh_tok)
            new_exp = int(time.time() + expires_in)
            if mailbox.get("id"):
                conn = get_connection()
                cur = conn.cursor()
                cur.execute(
                    "UPDATE mailboxes SET access_token = ?, token_expires_at = ? WHERE id = ?",
                    (access_token, new_exp, mailbox["id"])
                )
                conn.commit()
                conn.close()
        except Exception as e:
            return "", f"Token refresh failed: {str(e)}"
    return access_token, ""

class CampaignRunner:
    """自动化发信执行器（支持单例与后台状态轮询）"""
    _instance = None

    def __init__(self):
        self.is_running = False
        self.stop_requested = False
        self.current_job = {
            "total": 0,
            "processed": 0,
            "success": 0,
            "failed": 0,
            "skipped": 0,
            "dry_run": False,
            "status": "idle", # idle, running, stopped, finished
            "current_lead": "",
            "logs": []
        }

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = CampaignRunner()
        return cls._instance

    def log(self, message: str, level: str = "INFO"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self.current_job["logs"].append(entry)
        if len(self.current_job["logs"]) > 200:
            self.current_job["logs"].pop(0)

    def stop(self):
        self.stop_requested = True
        self.log("Received stop signal, terminating after current task completes...", "WARN")

def render_template(template_str: str, lead: Dict[str, Any], mailbox: Dict[str, Any]) -> str:
    """
    渲染邮件模版变量
    支持: {first_name}, {company}, {title}, {country}, {category}, {custom_note},
          {sender_name}, {postal_address}, {opt_out_notice}
    """
    first_name = lead.get("first_name", "").strip() or "there"
    company = lead.get("company", "").strip() or "your company"
    country = lead.get("country", "").strip() or "your region"
    title = lead.get("title", "").strip() or "Team"
    category = lead.get("category", "").strip() or "business"
    custom_note = lead.get("custom_note", "").strip()
    
    sender_name = mailbox.get("sender_name", "").strip() or "Sales Director"
    postal_address = DEFAULT_SAFETY_CONFIG["default_postal_address"]
    opt_out_notice = DEFAULT_SAFETY_CONFIG["opt_out_notice"]

    text = template_str
    replacements = {
        "{first_name}": first_name,
        "{company}": company,
        "{country}": country,
        "{title}": title,
        "{category}": category,
        "{custom_note}": custom_note,
        "{sender_name}": sender_name,
        "{postal_address}": postal_address,
        "{opt_out_notice}": opt_out_notice
    }
    for k, v in replacements.items():
        text = text.replace(k, str(v))
    return text

def test_smtp_connection(mailbox: Dict[str, Any]) -> Tuple[bool, str]:
    """测试单个邮箱 SMTP 连通性与账号验证 (支持密码及 OAuth 2.0 XOAUTH2)"""
    host = mailbox["smtp_host"]
    port = int(mailbox["smtp_port"])
    ssl_mode = mailbox.get("ssl_mode", "starttls").lower()
    username = mailbox.get("username", "") or mailbox.get("email", "")
    password = mailbox.get("password", "")
    auth_type = mailbox.get("auth_type", "password")

    try:
        if ssl_mode == "ssl":
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(host, port, context=context, timeout=15)
        else:
            server = smtplib.SMTP(host, port, timeout=15)
            server.ehlo()
            if ssl_mode == "starttls":
                context = ssl.create_default_context()
                server.starttls(context=context)
                server.ehlo()

        if auth_type == "oauth2":
            token, err = get_token_for_mailbox(mailbox)
            if err or not token:
                server.quit()
                return False, f"OAuth token error: {err or 'Missing access token'}"
            auth_str = generate_xoauth2_string(mailbox["email"], token)
            code, resp = server.docmd("AUTH", "XOAUTH2 " + auth_str)
            server.quit()
            if code == 235:
                return True, "Microsoft XOAUTH2 SMTP authentication successful!"
            else:
                return False, f"XOAUTH2 failed ({code}): {resp.decode('utf-8', 'ignore')}"
        else:
            server.login(username, password)
            server.quit()
            return True, "SMTP connection and authentication successful!"
    except Exception as e:
        return False, f"Connection error: {str(e)}"

def send_single_email(mailbox: Dict[str, Any], to_email: str, subject: str, body_text: str) -> Tuple[bool, str]:
    """通过真实 SMTP 发送单封邮件"""
    host = mailbox["smtp_host"]
    port = int(mailbox["smtp_port"])
    ssl_mode = mailbox.get("ssl_mode", "starttls").lower()
    username = mailbox.get("username", "") or mailbox.get("email", "")
    password = mailbox.get("password", "")
    auth_type = mailbox.get("auth_type", "password")
    from_addr = f"{mailbox['sender_name']} <{mailbox['email']}>"

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_email
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain=mailbox["email"].split("@")[-1])
    
    # 遵循合规：增加 List-Unsubscribe 头部
    msg["List-Unsubscribe"] = f"<mailto:{mailbox['email']}?subject=unsubscribe>"

    # 优先纯文本（提高 B2B 冷邮件进箱率，避免被归类为促销邮件）
    part_text = MIMEText(body_text, "plain", "utf-8")
    msg.attach(part_text)

    # 将换行自动转换为基础 HTML 附带作为替代视图
    html_content = body_text.replace("\n", "<br>")
    part_html = MIMEText(f"<html><body><div style='font-family: Arial, sans-serif; font-size: 14px; line-height: 1.6; color: #222;'>{html_content}</div></body></html>", "html", "utf-8")
    msg.attach(part_html)

    try:
        if ssl_mode == "ssl":
            context = ssl.create_default_context()
            server = smtplib.SMTP_SSL(host, port, context=context, timeout=20)
        else:
            server = smtplib.SMTP(host, port, timeout=20)
            server.ehlo()
            if ssl_mode == "starttls":
                context = ssl.create_default_context()
                server.starttls(context=context)
                server.ehlo()

        if auth_type == "oauth2":
            token, err = get_token_for_mailbox(mailbox)
            if err or not token:
                server.quit()
                return False, f"OAuth token error: {err or 'Missing access token'}"
            auth_str = generate_xoauth2_string(mailbox["email"], token)
            code, resp = server.docmd("AUTH", "XOAUTH2 " + auth_str)
            if code != 235:
                server.quit()
                return False, f"XOAUTH2 failed ({code}): {resp.decode('utf-8', 'ignore')}"
        else:
            server.login(username, password)

        server.sendmail(mailbox["email"], [to_email], msg.as_string())
        server.quit()
        return True, "Delivered successfully"
    except Exception as e:
        return False, str(e)

def get_available_mailbox() -> Optional[Dict[str, Any]]:
    """获取一个仍未达到当日发送配额的活跃发件箱（按今日发送量最少优先轮换）"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    SELECT * FROM mailboxes 
    WHERE is_active = 1 AND sent_today < daily_limit
    ORDER BY sent_today ASC, id ASC
    LIMIT 1
    """)
    row = cur.fetchone()
    conn.close()
    return dict(row) if row else None

def get_eligible_leads_for_step(step_number: int) -> List[Dict[str, Any]]:
    """
    筛选符合该跟进阶段资格的客户：
    1. 状态必须为 active
    2. 邮箱不在退订黑名单中
    3. 如果是首封 (step_number == 1)，要求 current_step == 0
    4. 如果是后续跟进 (step_number > 1)，要求 current_step == step_number - 1，且与上次发信时间间隔 >= delay_days
    """
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT delay_days FROM sequences WHERE step_number = ?", (step_number,))
    seq_row = cur.fetchone()
    delay_days = seq_row[0] if seq_row else 3

    if step_number == 1:
        query = """
        SELECT l.* FROM leads l
        LEFT JOIN suppression_list s ON lower(l.email) = lower(s.email)
        WHERE l.status = 'active' 
          AND l.current_step = 0
          AND s.id IS NULL
        ORDER BY l.id ASC
        """
        cur.execute(query)
    else:
        # 后续跟进：需要检查时间差
        query = """
        SELECT l.* FROM leads l
        LEFT JOIN suppression_list s ON lower(l.email) = lower(s.email)
        WHERE l.status = 'active'
          AND l.current_step = ?
          AND s.id IS NULL
          AND (
              l.last_sent_at IS NULL 
              OR julianday('now', 'localtime') - julianday(l.last_sent_at) >= ?
          )
        ORDER BY l.last_sent_at ASC
        """
        cur.execute(query, (step_number - 1, delay_days))

    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def execute_campaign(step_number: int, dry_run: bool = True, target_lead_ids: Optional[List[int]] = None):
    """
    执行自动化发信任务
    - step_number: 阶段编号 (1~4)
    - dry_run: True 为模拟演练（不发真实邮件，校验逻辑与文案渲染）；False 为真实安全批量发送
    - target_lead_ids: 可选指定特定 Leads 发送
    """
    runner = CampaignRunner.get_instance()
    runner.is_running = True
    runner.stop_requested = False

    conn = get_connection()
    cur = conn.cursor()

    # 获取当前序列模版
    cur.execute("SELECT * FROM sequences WHERE step_number = ? AND is_active = 1", (step_number,))
    seq_row = cur.fetchone()
    if not seq_row:
        runner.log(f"Sequence Step {step_number} does not exist or is inactive!", "ERROR")
        runner.is_running = False
        conn.close()
        return

    sequence = dict(seq_row)

    # 获取目标客户列表
    if target_lead_ids and len(target_lead_ids) > 0:
        placeholders = ",".join("?" * len(target_lead_ids))
        cur.execute(f"SELECT * FROM leads WHERE id IN ({placeholders}) AND status = 'active'", target_lead_ids)
        leads = [dict(r) for r in cur.fetchall()]
    else:
        leads = get_eligible_leads_for_step(step_number)

    runner.current_job = {
        "total": len(leads),
        "processed": 0,
        "success": 0,
        "failed": 0,
        "skipped": 0,
        "dry_run": dry_run,
        "status": "running",
        "current_lead": "",
        "logs": []
    }

    mode_text = "[DRY-RUN 演练模式]" if dry_run else "[LIVE 正式发信模式]"
    runner.log(f"Started campaign for Step {step_number} ({sequence['step_name']}) in {mode_text}. Total leads: {len(leads)}")

    if len(leads) == 0:
        runner.log("No eligible leads found for this step.", "WARN")
        runner.current_job["status"] = "finished"
        runner.is_running = False
        conn.close()
        return

    for idx, lead in enumerate(leads):
        if runner.stop_requested:
            runner.log("Campaign execution stopped by user request.", "WARN")
            runner.current_job["status"] = "stopped"
            break

        runner.current_job["current_lead"] = lead["email"]
        runner.current_job["processed"] = idx + 1

        # 检查是否退订黑名单
        cur.execute("SELECT id FROM suppression_list WHERE lower(email) = lower(?)", (lead["email"],))
        if cur.fetchone():
            runner.log(f"Skipping {lead['email']} (in suppression list)", "WARN")
            runner.current_job["skipped"] += 1
            continue

        # 获取可用发信箱
        if not dry_run:
            mailbox = get_available_mailbox()
            if not mailbox:
                runner.log("ALL active mailboxes have reached their daily limit! Pausing campaign to protect deliverability.", "ERROR")
                runner.current_job["status"] = "stopped"
                break
        else:
            # 演练模式下使用虚拟发件人
            mailbox = {
                "id": 0,
                "email": "demo.sender@domain.com",
                "sender_name": "Evan Huang",
                "daily_limit": 25,
                "sent_today": 0
            }

        # 渲染标题与正文
        rendered_subject = render_template(sequence["subject"], lead, mailbox)
        rendered_body = render_template(sequence["body_template"], lead, mailbox)

        if dry_run:
            # 模拟发信
            time.sleep(0.5) # 极小延迟仅供 UI 展示
            status = "dry_run"
            err_msg = ""
            runner.log(f"[Dry-Run] Rendered email for {lead['email']} (Company: {lead.get('company')})")
            runner.current_job["success"] += 1
            
            # 记录日志
            cur.execute("""
            INSERT INTO send_logs (lead_id, lead_email, mailbox_id, mailbox_email, step_number, subject, status, error_message)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (lead["id"], lead["email"], mailbox["id"], mailbox["email"], step_number, rendered_subject, status, err_msg))
            
            # 在演练中更新 current_step 和 last_sent_at
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cur.execute("""
            UPDATE leads 
            SET current_step = ?, last_sent_at = ? 
            WHERE id = ?
            """, (step_number, now_str, lead["id"]))
            conn.commit()

        else:
            # 真实发信
            ok, msg = send_single_email(mailbox, lead["email"], rendered_subject, rendered_body)
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if ok:
                runner.log(f"[Sent] {lead['email']} via {mailbox['email']} (Step {step_number})", "SUCCESS")
                runner.current_job["success"] += 1
                
                # 更新邮箱已发送计数
                cur.execute("UPDATE mailboxes SET sent_today = sent_today + 1 WHERE id = ?", (mailbox["id"],))
                # 更新客户当前阶段
                cur.execute("UPDATE leads SET current_step = ?, last_sent_at = ? WHERE id = ?", (step_number, now_str, lead["id"]))
                # 记录日志
                cur.execute("""
                INSERT INTO send_logs (lead_id, lead_email, mailbox_id, mailbox_email, step_number, subject, status, error_message)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (lead["id"], lead["email"], mailbox["id"], mailbox["email"], step_number, rendered_subject, "success", ""))
                conn.commit()

                # 发信安全防风控延迟（在 min_delay 和 max_delay 之间随机等待）
                if idx < len(leads) - 1 and not runner.stop_requested:
                    jitter = random.uniform(DEFAULT_SAFETY_CONFIG["min_delay_seconds"], DEFAULT_SAFETY_CONFIG["max_delay_seconds"])
                    runner.log(f"Pacing: waiting {jitter:.1f}s before next send to protect domain health...")
                    time.sleep(jitter)
            else:
                runner.log(f"[Failed] {lead['email']} error: {msg}", "ERROR")
                runner.current_job["failed"] += 1
                cur.execute("""
                INSERT INTO send_logs (lead_id, lead_email, mailbox_id, mailbox_email, step_number, subject, status, error_message)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (lead["id"], lead["email"], mailbox["id"], mailbox["email"], step_number, rendered_subject, "failed", msg))
                conn.commit()

    if runner.current_job["status"] != "stopped":
        runner.current_job["status"] = "finished"
    runner.log(f"Campaign finished. Sent: {runner.current_job['success']}, Failed: {runner.current_job['failed']}, Skipped: {runner.current_job['skipped']}")
    runner.is_running = False
    conn.close()
