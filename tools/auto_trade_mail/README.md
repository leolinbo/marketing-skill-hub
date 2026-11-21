# Auto Trade Mail - 自动化外贸邮件工作站

一个遵循 `marketing/skills/cold-outreach` 与 `marketing/skills/email-marketing` 核心规范的**本地化自动化外贸邮件系统**。开箱即用，无需配置复杂的外部服务，直接在本地双击即可运行。

---

## 🌟 核心特性与营销规范遵循

1. **合规第一 (CAN-SPAM & GDPR)**：
   - 自动在邮件底部内嵌物理实体公司地址与清晰退订引导（如 `Reply "no thanks" to be removed`）；
   - **全局退订黑名单强拦截（Suppression List）**：一旦客户退订或要求不要跟进，全局阻断后续所有序列，严格保护发件域名信用。
2. **多邮箱轮换与每日配额保护 (Mailbox Pool)**：
   - 支持添加多个发件邮箱（Gmail、Outlook、腾讯企业邮、阿里企业邮、网易企业邮或专有外贸域名）；
   - 严格遵守单邮箱每日安全上限（默认 25 封/天），防止单邮箱突发流量被服务商封禁。
3. **随机防风控发信间隔 (Random Jitter)**：
   - 每次发信之间自动在 25~65 秒之间随机浮动，模拟真人发信节奏，显著降低被识别为机器群发并被打入垃圾箱的概率。
4. **4 阶段梯度自动化跟进 (4-Step Outreach Matrix)**：
   - **Step 1 (Day 0)**：痛点共鸣与微测样提议（首封纯文本高进箱率）。
   - **Step 2 (Day 3)**：同主题（In-thread Re:）跟进，补充核心电气认证、协议兼容与免打扰说明。
   - **Step 3 (Day 7)**：供应链痛点打击（7 天现货、低 MOQ、避免断货）。
   - **Step 4 (Day 14)**：优雅收尾 Break-up 邮件。
5. **双重发信模式**：
   - **【安全演练 Dry-Run】**：100% 走通全流程与变量替换测试，不发真实邮件、不扣配额；
   - **【正式安全发送 LIVE】**：连接配置的发信邮箱真实投递。

---

## 🚀 快速启动

### 方式一：双击启动 (推荐)
直接在资源管理器中双击运行：
👉 `d:\marketing\tools\auto_trade_mail\run.bat` (仅本地访问)
👉 `d:\marketing\tools\auto_trade_mail\run_with_cloudflare.bat` (本地 + Cloudflare 全球公网访问)

浏览器打开 Web 控制面板：`http://127.0.0.1:8765` 或 Cloudflare 提供的公网 HTTPS 链接。

### 方式二：命令行启动
```bash
cd d:\marketing\tools\auto_trade_mail
python server.py
# 若需要公网访问，同时运行：
.\cloudflared.exe tunnel --protocol http2 --url http://localhost:8765
```

### 方式三：CLI 无界面直接调用
```bash
cd d:\marketing\tools\auto_trade_mail

# 1. 查看系统统计与今日配额
python cli.py status

# 2. 导入客户名单 (CSV 或 Excel)
python cli.py import your_leads.csv

# 3. 运行演练模式
python cli.py run --step 1

# 4. 运行真实发信
python cli.py run --step 1 --live
```

---

## ⚙️ 常见发信邮箱 SMTP 配置指南

| 邮箱类型 | SMTP 主机 | 端口 | 加密协议 | 密码填写要求 |
|---|---|---|---|---|
| **Gmail** | `smtp.gmail.com` | `587` | STARTTLS | 需在 Google 账号中开启两步验证并生成 **应用专用密码 (App Password)** |
| **Outlook / Office 365** | `smtp.office365.com` | `587` | STARTTLS | 微软账号应用密码 |
| **网易企业邮** | `smtphm.qiye.163.com` | `465` | SSL | 客户端专用授权码 |
| **腾讯企业邮** | `smtp.exmail.qq.com` | `465` | SSL | 企业微信/邮箱客户端安全专用密码 |

---

## 📁 目录文件结构

```
tools/auto_trade_mail/
├── config.py             # 全局安全策略（每日上限、防风控延迟、物理地址）
├── db.py                 # SQLite 存储层与默认外贸 4-Step 序列
├── mailer.py             # 核心发信引擎、模版变量渲染与轮换算法
├── importer.py           # CSV / Excel 客户清洗与去重导入器
├── server.py             # 轻量级本地 Web API 服务 (基于 Python 标准库)
├── cli.py                # 命令行独立运行入口
├── run.bat               # Windows 双击一键启动脚本
├── run.ps1               # PowerShell 启动脚本
├── static/
│   └── index.html        # 现代化单页面控制台 (SPA)
└── data/
    └── trade_mail.db     # 本地持久化数据库文件
```
