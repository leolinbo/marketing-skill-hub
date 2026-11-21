# -*- coding: utf-8 -*-
"""
Auto Trade Mail - 自动化外贸邮件工具配置
遵循 marketing 知识库规范 (skills/cold-outreach)
"""
import os
from pathlib import Path

# 基础目录
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# 数据库路径
DB_PATH = DATA_DIR / "trade_mail.db"

# Web 服务配置（云端环境自动读取 PORT 和 HOST）
WEB_HOST = os.environ.get("HOST", "0.0.0.0")
WEB_PORT = int(os.environ.get("PORT", 8765))

# 外贸营销发信安全红线 (来自 marketing/skills/cold-outreach)
DEFAULT_SAFETY_CONFIG = {
    # 单个邮箱每日安全发送上限（新邮箱/预热期建议10-25封，稳定期30封以内）
    "max_emails_per_mailbox_per_day": 25,
    # 发送间隔（秒）：随机在 min_delay 和 max_delay 之间波动，模拟真人操作
    "min_delay_seconds": 25,
    "max_delay_seconds": 65,
    # 失败重试次数
    "max_retries": 2,
    # 默认发件人物理地址（CAN-SPAM 合规必需）
    "default_postal_address": "Encore Lighting Co., Ltd. · Industrial High-Tech Zone, Shenzhen, China",
    # 默认退订声明
    "opt_out_notice": "Not interested or not the right person? Simply reply 'no thanks' or click unsubscribe to be removed immediately."
}
