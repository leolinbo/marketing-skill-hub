# -*- coding: utf-8 -*-
"""
Email Warm-up Engine (自动化邮箱预热与健康养号引擎)
模拟自然商务沟通往来，提升发信域名与新邮箱权重
"""
import time
import random
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, make_msgid
from typing import List, Dict, Any, Tuple

from db import get_connection
from mailer import get_token_for_mailbox
from oauth_outlook import generate_xoauth2_string
import smtplib
import ssl

# 预置高质感自然商务日常沟通语料库（模拟真人正常来往，杜绝模板推销痕迹）
WARMUP_TOPICS = [
    {
        "subject": "Quick check on the project schedule",
        "body": "Hi,\n\nJust following up on our project milestones for this week. Could you review the timeline when you get a chance?\n\nLet me know if we need to adjust any dates.\n\nBest regards,"
    },
    {
        "subject": "Updated meeting notes from yesterday",
        "body": "Hi there,\n\nI have summarized the main points discussed during yesterday's sync. Please take a look at your convenience and let me know if I missed anything important.\n\nThanks!"
    },
    {
        "subject": "Question regarding the technical specifications",
        "body": "Hi,\n\nGoing over the latest spec sheet. I noticed a few parameters regarding the power supply testing. Are these already finalized or still pending review?\n\nTalk soon,"
    },
    {
        "subject": "Sharing the quarterly review document",
        "body": "Hello,\n\nHope your week is going well. I'm sharing the preliminary overview for the quarterly review. Feel free to add your thoughts.\n\nBest,"
    },
    {
        "subject": "Quick note regarding the upcoming exhibition",
        "body": "Hi,\n\nQuick question regarding the booth arrangement and sample presentation for the trade show. Do you have 5 minutes later this afternoon to coordinate?\n\nRegards,"
    },
    {
        "subject": "Sample test results overview",
        "body": "Hi,\n\nThe optical and thermal consistency testing on the latest production batch came back looking very solid. I will have the full report compiled shortly.\n\nBest,"
    }
]

class WarmupRunner:
    _instance = None

    def __init__(self):
        self.is_running = False
        self.stop_requested = False
        self.current_job = {
            "total": 0,
            "processed": 0,
            "success": 0,
            "failed": 0,
            "status": "idle", # idle, running, stopped, finished
            "current_action": "",
            "logs": []
        }

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = WarmupRunner()
        return cls._instance

    def log(self, message: str, level: str = "INFO"):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] [{level}] {message}"
        self.current_job["logs"].append(entry)
        if len(self.current_job["logs"]) > 200:
            self.current_job["logs"].pop(0)

    def stop(self):
        self.stop_requested = True
        self.log("收到停止预热指令，当前单封发完后将自动终止...", "WARN")

def send_warmup_single(mailbox: Dict[str, Any], to_email: str, subject: str, body_text: str, max_retries: int = 3) -> Tuple[bool, str]:
    """发送一封预热邮件 (带抗丢包智能重试)"""
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

    # 预热邮件使用自然纯文本，进箱率最高
    msg.attach(MIMEText(body_text, "plain", "utf-8"))

    last_error = ""
    for attempt in range(1, max_retries + 1):
        try:
            if ssl_mode == "ssl":
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(host, port, context=context, timeout=25)
            else:
                server = smtplib.SMTP(host, port, timeout=25)
                server.ehlo()
                if ssl_mode == "starttls":
                    context = ssl.create_default_context()
                    server.starttls(context=context)
                    server.ehlo()

            if auth_type == "oauth2":
                token, err = get_token_for_mailbox(mailbox)
                if err or not token:
                    server.quit()
                    return False, f"OAuth Token 错误: {err}"
                auth_str = generate_xoauth2_string(mailbox["email"], token)
                code, resp = server.docmd("AUTH", "XOAUTH2 " + auth_str)
                if code != 235:
                    server.quit()
                    return False, f"XOAUTH2 失败 ({code}): {resp.decode('utf-8', 'ignore')}"
            else:
                server.login(username, password)

            server.sendmail(mailbox["email"], [to_email], msg.as_string())
            server.quit()
            return True, "Delivered"
        except Exception as e:
            last_error = str(e)
            if attempt < max_retries:
                time.sleep(2)  # 遇到国内网络瞬时丢包，间隔 2 秒重试

    return False, last_error

def execute_warmup_task(target_emails: List[str], count_per_mailbox: int = 2, min_delay: int = 25, max_delay: int = 50):
    """
    执行自动化养号预热流程：
    - 遍历所有活跃发件箱
    - 每个发件箱随机抽取预热接收邮箱，发送自然日常商务邮件
    - 带有随机时间抖动，完全模拟真人正常来往
    """
    runner = WarmupRunner.get_instance()
    runner.is_running = True
    runner.stop_requested = False

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM mailboxes WHERE is_active = 1")
    mailboxes = [dict(r) for r in cur.fetchall()]

    if not mailboxes:
        runner.log("未找到活跃的发件箱，请先在发件箱池中配置并启用邮箱！", "ERROR")
        runner.is_running = False
        conn.close()
        return

    if not target_emails:
        runner.log("预热目标邮箱列表为空，请填写您的预热接收邮箱！", "ERROR")
        runner.is_running = False
        conn.close()
        return

    # 计算总任务量
    total_tasks = len(mailboxes) * count_per_mailbox
    runner.current_job = {
        "total": total_tasks,
        "processed": 0,
        "success": 0,
        "failed": 0,
        "status": "running",
        "current_action": "准备开始预热任务...",
        "logs": []
    }

    runner.log(f"🔥 启动自动化预热养号！发件箱: {len(mailboxes)} 个 | 每个预热 {count_per_mailbox} 封 | 总计: {total_tasks} 封")

    for mbox in mailboxes:
        if runner.stop_requested:
            break

        runner.log(f"--- 正在使用发件箱: {mbox['email']} 发起预热 ---")
        for i in range(count_per_mailbox):
            if runner.stop_requested:
                break

            dest_email = random.choice(target_emails).strip()
            topic = random.choice(WARMUP_TOPICS)
            subject = topic["subject"]
            # 附带发件人签名
            body = f"{topic['body']}\n\n{mbox['sender_name']}\nEncore Lighting Team"

            runner.current_job["current_action"] = f"{mbox['email']} ➔ {dest_email}"
            runner.log(f"正在发送预热邮件: {mbox['email']} ➔ {dest_email} (主题: {subject})")

            ok, err = send_warmup_single(mbox, dest_email, subject, body)
            runner.current_job["processed"] += 1

            if ok:
                runner.current_job["success"] += 1
                runner.log(f"✅ [成功送达] {dest_email} (来自 {mbox['email']})", "SUCCESS")
                
                # 记录到系统发信日志中标记为 warmup
                cur.execute("""
                INSERT INTO send_logs (lead_id, lead_email, mailbox_id, mailbox_email, step_number, subject, status, error_message)
                VALUES (0, ?, ?, ?, 99, ?, 'warmup', '')
                """, (dest_email, mbox["id"], mbox["email"], subject))
                # 消耗一次发件箱额度
                cur.execute("UPDATE mailboxes SET sent_today = sent_today + 1 WHERE id = ?", (mbox["id"],))
                conn.commit()

                # 随机防风控间隔
                if (runner.current_job["processed"] < total_tasks) and not runner.stop_requested:
                    jitter = random.uniform(min_delay, max_delay)
                    runner.log(f"模拟真人发信节奏：等待 {jitter:.1f} 秒后发送下一封...")
                    time.sleep(jitter)
            else:
                runner.current_job["failed"] += 1
                runner.log(f"❌ [发送失败] {dest_email} 原因: {err}", "ERROR")
                cur.execute("""
                INSERT INTO send_logs (lead_id, lead_email, mailbox_id, mailbox_email, step_number, subject, status, error_message)
                VALUES (0, ?, ?, ?, 99, ?, 'failed', ?)
                """, (dest_email, mbox["id"], mbox["email"], subject, err))
                conn.commit()

    conn.close()
    runner.current_job["status"] = "stopped" if runner.stop_requested else "finished"
    runner.log(f"🎉 预热任务全部结束！成功送达: {runner.current_job['success']} 封, 失败: {runner.current_job['failed']} 封")
    runner.is_running = False
