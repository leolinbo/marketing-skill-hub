# -*- coding: utf-8 -*-
"""
Database Management Layer for Auto Trade Mail
SQLite 数据库模型与基础操作
"""
import sqlite3
import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
from config import DB_PATH, DEFAULT_SAFETY_CONFIG

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """初始化数据库表结构与默认序列"""
    conn = get_connection()
    cur = conn.cursor()

    # 1. 客户线索表 (Leads)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        first_name TEXT DEFAULT '',
        company TEXT DEFAULT '',
        title TEXT DEFAULT '',
        country TEXT DEFAULT '',
        category TEXT DEFAULT 'General',
        custom_note TEXT DEFAULT '',
        current_step INTEGER DEFAULT 0,
        status TEXT DEFAULT 'active', -- active, paused, replied, unsubscribed, bounced, completed
        last_sent_at TEXT,
        next_eligible_at TEXT,
        created_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
    """)

    # 2. 发件箱池配置表 (Mailbox Pool)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS mailboxes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        sender_name TEXT NOT NULL,
        smtp_host TEXT NOT NULL,
        smtp_port INTEGER NOT NULL DEFAULT 587,
        ssl_mode TEXT NOT NULL DEFAULT 'starttls', -- starttls, ssl, none
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        daily_limit INTEGER DEFAULT 25,
        sent_today INTEGER DEFAULT 0,
        last_reset_date TEXT DEFAULT (date('now', 'localtime')),
        is_active INTEGER DEFAULT 1,
        notes TEXT DEFAULT ''
    )
    """)

    # 3. 多阶段跟进序列模版表 (Outreach Sequences)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS sequences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        step_number INTEGER NOT NULL UNIQUE,
        step_name TEXT NOT NULL,
        delay_days INTEGER NOT NULL DEFAULT 3,
        subject TEXT NOT NULL,
        body_template TEXT NOT NULL,
        is_thread_reply INTEGER DEFAULT 1,
        is_active INTEGER DEFAULT 1
    )
    """)

    # 4. 发信详细日志表 (Send Logs)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS send_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        lead_id INTEGER,
        lead_email TEXT,
        mailbox_id INTEGER,
        mailbox_email TEXT,
        step_number INTEGER,
        subject TEXT,
        status TEXT, -- success, failed, dry_run
        error_message TEXT DEFAULT '',
        sent_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
    """)

    # 5. 黑名单与退订表 (Suppression List)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS suppression_list (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        reason TEXT DEFAULT 'Unsubscribed',
        added_at TEXT DEFAULT (datetime('now', 'localtime'))
    )
    """)

    # 6. 系统全局设置 (Settings)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)

    conn.commit()

    # 检查并填充默认外贸序列模版 (基于 marketing/skills/cold-outreach 规范)
    cur.execute("SELECT COUNT(*) FROM sequences")
    if cur.fetchone()[0] == 0:
        seed_default_sequences(cur)
        conn.commit()

    # 检查并填充默认示例客户数据（方便用户开箱预览）
    cur.execute("SELECT COUNT(*) FROM leads")
    if cur.fetchone()[0] == 0:
        seed_sample_leads(cur)
        conn.commit()

    conn.close()

def seed_default_sequences(cur: sqlite3.Cursor):
    """注入来自 marketing 知识库的高转化外贸序列"""
    seqs = [
        (
            1,
            "Step 1: 价值锚定与测样提议 (首封)",
            0,
            "Quick question regarding {company}'s lighting line",
            """Hi {first_name},

Saw that {company} specializes in architectural lighting projects in {country}. {custom_note}

We engineer low-voltage 48V magnetic track and motorized spot systems directly for engineering contractors and design distributors. Our systems maintain long-term optical consistency (SDCM < 3) with flexible low MOQs starting from 50 units.

A regional distributor recently deployed our 48V linear system in several boutique retail spaces with zero driver failure after 18 months of continuous operation.

Would you be open to receiving our 1-page technical spec sheet or a free demo kit of our latest optics?

Best regards,
{sender_name}
Encore Lighting Co., Ltd.
{postal_address}

{opt_out_notice}""",
            0,
            1
        ),
        (
            2,
            "Step 2: 补充细节与免打扰打消顾虑 (第 3 天跟进)",
            3,
            "Re: Quick question regarding {company}'s lighting line",
            """Hi {first_name},

One quick detail I forgot to mention in my previous note:

All our magnetic fixtures support seamless DALI-2, Tuya/Zigbee, and 0-10V dimming protocols out of the box, making them plug-and-play for smart commercial retrofits without rewiring.

Happy to share our recent IES test files if that helps your project planning.

Best,
{sender_name}""",
            1,
            1
        ),
        (
            3,
            "Step 3: 提供高价值方案/避免断货 (第 7 天跟进)",
            4,
            "Re: Quick question regarding {company}'s lighting line",
            """Hi {first_name},

Many procurement managers tell us their biggest pain point is the 6-8 week lead time for specialized lighting fixtures. 

Because we keep modular components in pre-assembled stock, standard orders ship in under 7 business days, with customizable beam angles (15°/24°/36°/60°).

Would this type of supply reliability be useful for {company}'s upcoming projects this quarter?

{sender_name}""",
            1,
            1
        ),
        (
            4,
            "Step 4: 礼貌收尾 Break-up (第 14 天关闭沟通)",
            7,
            "Re: Quick question regarding {company}'s lighting line",
            """Hi {first_name},

I don't want to clutter your inbox, so I'll stop following up for now.

If you ever need reliable architectural track lights or custom optical solutions down the road, please feel free to keep my contact information handy.

Wishing you and {company} continued success!

Best regards,
{sender_name}
{postal_address}""",
            1,
            1
        )
    ]

    cur.executemany("""
    INSERT INTO sequences (step_number, step_name, delay_days, subject, body_template, is_thread_reply, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, seqs)

def seed_sample_leads(cur: sqlite3.Cursor):
    """注入示例 Leads"""
    samples = [
        ("carlos.lighting@example.com", "Carlos", "Barcelona LED", "Procurement Director", "Spain", "Distributor", "Noticed your impressive showroom and focus on 48V magnetic systems.", 0, "active"),
        ("elena.design@example.com", "Elena", "Arkultura Architecture", "Lead Architect", "Philippines", "Architectural Firm", "Loved your modern minimalist interior designs in Makati.", 0, "active"),
        ("dimitar.stefanov@example.com", "Dimitar", "D3 Design Studio", "Engineering Lead", "Bulgaria", "Engineering Studio", "Observed your commercial lighting project portfolio.", 0, "active")
    ]
    cur.executemany("""
    INSERT INTO leads (email, first_name, company, title, country, category, custom_note, current_step, status)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, samples)

# --- 数据库操作函数 ---

def reset_daily_counters_if_needed(cur: sqlite3.Cursor):
    """每日重置邮箱已发送计数"""
    today_str = datetime.date.today().isoformat()
    cur.execute("""
    UPDATE mailboxes 
    SET sent_today = 0, last_reset_date = ? 
    WHERE last_reset_date != ?
    """, (today_str, today_str))

def get_dashboard_stats() -> Dict[str, Any]:
    conn = get_connection()
    cur = conn.cursor()
    reset_daily_counters_if_needed(cur)
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM leads")
    total_leads = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM leads WHERE status = 'active'")
    active_leads = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM leads WHERE status = 'replied'")
    replied_leads = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM leads WHERE status = 'unsubscribed'")
    unsub_leads = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM leads WHERE status = 'bounced'")
    bounced_leads = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM mailboxes WHERE is_active = 1")
    active_mailboxes = cur.fetchone()[0]

    cur.execute("SELECT SUM(sent_today) FROM mailboxes WHERE is_active = 1")
    res_today = cur.fetchone()[0]
    sent_today = res_today if res_today else 0

    cur.execute("SELECT COUNT(*) FROM suppression_list")
    suppressed_count = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM send_logs WHERE date(sent_at) = date('now', 'localtime')")
    logs_today = cur.fetchone()[0]

    conn.close()
    return {
        "total_leads": total_leads,
        "active_leads": active_leads,
        "replied_leads": replied_leads,
        "unsub_leads": unsub_leads,
        "bounced_leads": bounced_leads,
        "active_mailboxes": active_mailboxes,
        "sent_today": sent_today,
        "suppressed_count": suppressed_count,
        "logs_today": logs_today
    }
