# -*- coding: utf-8 -*-
"""
Command Line Interface for Auto Trade Mail
支持无界面终端环境下的快捷操作与批量任务
"""
import sys
import argparse
from pathlib import Path
from db import init_db, get_dashboard_stats, get_connection
from mailer import execute_campaign, CampaignRunner, test_smtp_connection
from importer import parse_csv_content, import_leads_from_rows, parse_excel_file

def cmd_status(args):
    init_db()
    stats = get_dashboard_stats()
    print("==================================================")
    print(" Auto Trade Mail - 系统状态简报")
    print("==================================================")
    print(f" 总线索数 (Total Leads):       {stats['total_leads']}")
    print(f" 活跃跟进中 (Active):          {stats['active_leads']}")
    print(f" 客户已回复 (Replied):         {stats['replied_leads']}")
    print(f" 客户已退订 (Unsubscribed):    {stats['unsub_leads']}")
    print(f" 活跃发信箱 (Mailboxes):       {stats['active_mailboxes']}")
    print(f" 今日已发信数 (Sent Today):    {stats['sent_today']}")
    print(f" 全局退订黑名单 (Suppressed):  {stats['suppressed_count']}")
    print("==================================================")

def cmd_run(args):
    init_db()
    step = args.step
    dry_run = not args.live
    print(f">> 启动发信任务: Step {step} | 模式: {'[DRY-RUN 演练]' if dry_run else '[LIVE 正式发送]'}")
    execute_campaign(step_number=step, dry_run=dry_run)

def cmd_import(args):
    init_db()
    path = Path(args.file)
    if not path.exists():
        print(f"Error: 文件不存在 {args.file}")
        return

    print(f">> 正在解析并导入: {path.name}")
    if path.suffix.lower() == ".csv":
        with open(path, "r", encoding="utf-8-sig", errors="ignore") as f:
            rows = parse_csv_content(f.read())
    elif path.suffix.lower() in [".xlsx", ".xls"]:
        rows = parse_excel_file(path)
    else:
        print("Error: 仅支持 .csv 或 .xlsx 文件格式")
        return

    res = import_leads_from_rows(rows)
    print(">> 导入清洗完成:")
    print(f"   新增线索: {res['inserted']}")
    print(f"   更新线索: {res['updated']}")
    print(f"   跳过黑名单: {res['skipped_suppressed']}")
    print(f"   非法邮箱格式: {res['invalid_emails']}")

def main():
    parser = argparse.ArgumentParser(description="Auto Trade Mail CLI")
    subparsers = parser.add_subparsers(dest="command", help="可用子命令")

    # status
    subparsers.add_parser("status", help="查看系统状态与发信统计")

    # run
    run_parser = subparsers.add_parser("run", help="执行自动化外贸发信")
    run_parser.add_argument("--step", type=int, default=1, help="发信阶段 (1~4)")
    run_parser.add_argument("--live", action="store_true", help="启用正式真实发信模式 (默认演练模式)")

    # import
    import_parser = subparsers.add_parser("import", help="导入 CSV 或 Excel 客户名单")
    import_parser.add_argument("file", help="CSV 或 XLSX 文件路径")

    args = parser.parse_args()
    if args.command == "status":
        cmd_status(args)
    elif args.command == "run":
        cmd_run(args)
    elif args.command == "import":
        cmd_import(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
