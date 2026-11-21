# -*- coding: utf-8 -*-
"""
Lead Importer & Data Cleaning
支持 CSV、Excel (.xlsx) 智能表头匹配与去重清洗
"""
import re
import csv
import io
from pathlib import Path
from typing import Dict, Any, List, Tuple
from db import get_connection

EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

COLUMN_MAPPING = {
    "email": ["email", "e-mail", "mail", "邮箱", "电子邮箱", "mail address"],
    "first_name": ["first_name", "firstname", "name", "contact", "contact_name", "联系人", "名字", "姓名"],
    "company": ["company", "company_name", "organization", "公司", "企业名称", "客户名称"],
    "title": ["title", "job_title", "position", "role", "职位", "头衔", "岗位"],
    "country": ["country", "region", "market", "国家", "地区", "市场"],
    "category": ["category", "type", "tag", "industry", "分类", "行业", "类别", "客户类型"],
    "custom_note": ["custom_note", "note", "notes", "observation", "remark", "备注", "观察细节", "调研记录"]
}

def normalize_header(header: str) -> str:
    cleaned = header.strip().lower().replace(" ", "_").replace("-", "_")
    for standard_col, aliases in COLUMN_MAPPING.items():
        if cleaned in aliases:
            return standard_col
    return cleaned

def is_valid_email(email: str) -> bool:
    if not email or not isinstance(email, str):
        return False
    return bool(EMAIL_REGEX.match(email.strip()))

def import_leads_from_rows(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """批量清洗并写入数据库"""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT lower(email) FROM suppression_list")
    suppressed = set(r[0] for r in cur.fetchall())

    cur.execute("SELECT lower(email) FROM leads")
    existing_leads = set(r[0] for r in cur.fetchall())

    inserted = 0
    updated = 0
    skipped = 0
    invalid = 0

    for raw_row in rows:
        row = {normalize_header(k): str(v).strip() if v is not None else "" for k, v in raw_row.items()}
        email = row.get("email", "").strip()

        if not is_valid_email(email):
            invalid += 1
            continue

        email_lower = email.lower()

        if email_lower in suppressed:
            skipped += 1
            continue

        first_name = row.get("first_name", "")
        company = row.get("company", "")
        title = row.get("title", "")
        country = row.get("country", "")
        category = row.get("category", "") or "General"
        custom_note = row.get("custom_note", "")

        if email_lower in existing_leads:
            cur.execute("""
            UPDATE leads 
            SET first_name = COALESCE(NULLIF(?, ''), first_name),
                company = COALESCE(NULLIF(?, ''), company),
                title = COALESCE(NULLIF(?, ''), title),
                country = COALESCE(NULLIF(?, ''), country),
                category = COALESCE(NULLIF(?, ''), category),
                custom_note = COALESCE(NULLIF(?, ''), custom_note)
            WHERE lower(email) = ?
            """, (first_name, company, title, country, category, custom_note, email_lower))
            updated += 1
        else:
            cur.execute("""
            INSERT INTO leads (email, first_name, company, title, country, category, custom_note)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (email, first_name, company, title, country, category, custom_note))
            existing_leads.add(email_lower)
            inserted += 1

    conn.commit()
    conn.close()

    return {
        "inserted": inserted,
        "updated": updated,
        "skipped_suppressed": skipped,
        "invalid_emails": invalid,
        "total_processed": len(rows)
    }

def parse_csv_content(content_str: str) -> List[Dict[str, Any]]:
    """解析 CSV 文本"""
    f = io.StringIO(content_str)
    reader = csv.DictReader(f)
    return [row for row in reader]

def parse_excel_file(file_path: Path) -> List[Dict[str, Any]]:
    """使用 openpyxl 解析 Excel 文件"""
    import openpyxl
    wb = openpyxl.load_workbook(file_path, data_only=True)
    sheet = wb.active
    rows = list(sheet.iter_rows(values_only=True))
    if not rows or len(rows) < 2:
        return []

    headers = [str(h).strip() if h is not None else f"col_{i}" for i, h in enumerate(rows[0])]
    result = []
    for r in rows[1:]:
        if not any(r):
            continue
        row_dict = {}
        for idx, val in enumerate(r):
            if idx < len(headers):
                row_dict[headers[idx]] = val
        result.append(row_dict)
    return result
