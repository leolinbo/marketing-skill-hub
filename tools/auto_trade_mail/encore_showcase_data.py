# -*- coding: utf-8 -*-
"""
Encore Lighting Project Showcase & AIDA Cadence Data
提供 4 阶段跟进体系模版、真实买家线索库及本地网盘资源对应
"""
import os
import base64

ICONS_DIR = r"\\192.168.1.18\市场部\部门资料\11、社媒运营标准资料\01 标准资料\02 社媒图标"
BANNER_DIR = r"\\192.168.1.18\市场部\市场部——业务部\02 营销资料\06 2026邮件推广图片(邮签)"

# 产品与对应网盘推荐图映射
PRODUCT_BANNER_MAP = {
    "DELLA": os.path.join(BANNER_DIR, r"DELLA\DELLA-mini.jpg"),
    "48V 磁吸轨道 / Magnetic": os.path.join(BANNER_DIR, r"Magnetic\Magnetic-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"Magnetic\Magnetic-1.jpg")) else "",
    "VEGA": os.path.join(BANNER_DIR, r"VEGA\VEGA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"VEGA\VEGA-1.jpg")) else "",
    "AVA": os.path.join(BANNER_DIR, r"AVA\AVA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"AVA\AVA-1.jpg")) else "",
    "ELLA": os.path.join(BANNER_DIR, r"ELLA\ELLA-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"ELLA\ELLA-1.jpg")) else "",
    "GALAXY": os.path.join(BANNER_DIR, r"GALAXY\GALAXY-1.jpg") if os.path.exists(os.path.join(BANNER_DIR, r"GALAXY\GALAXY-1.jpg")) else "",
}

# 4 阶段自动化跟进体系定义
ENCORE_SEQUENCES = [
    {
        "step_number": 1,
        "step_name": "Step 1: 痛点疑问开场 (轻量纯文本·高进箱率)",
        "delay_days": 0,
        "is_thread_reply": 0,
        "subject": "{subject_step1}",
        "body_template": """Hi {first_name},

{pain_point_opener}

We build architectural fixtures in Shenzhen specifically engineered to solve these optical and installation challenges for commercial contractors and project designers.

Would a quick spec sheet or a couple of project mock-up photos be useful to see how other schemes handle this?

Best regards,

Bob | International Sales Executive@Encore
sales@encore-tech.com | +86(0)755 2322 4735 | www.encore-tech.com
2/F, Bldg 8th, Zhengzhong Industrial Park, Bao'an Dist, Shenzhen, China 518103"""
    },
    {
        "step_number": 2,
        "step_name": "Step 2: AIDA 拳头单品击穿 (Slogan+卖点+样品行动召唤)",
        "delay_days": 3,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

Following up on my previous note regarding {company}'s architectural lighting schemes.

Now, you have {recommended_product}, you have the solution!

{product_bullets}

Act today! Samples are available upon confirmation. Would you like a sample kit sent to your office for your upcoming project mock-up?

Best regards,

Bob
International Sales Executive@Encore

T: +86(0)755 2322 4735    M: +86.135.0005.2091 (WhatsApp/WeChat)
E: sales@encore-tech.com    W: www.encore-tech.com
A: 2/F, Bldg 8th, Zhengzhong Industrial Park, Qiaotou Community, Fuyong, Bao'an Dist, Shenzhen, China 518103"""
    },
    {
        "step_number": 3,
        "step_name": "Step 3: 案例与供应链背书 (Nike连锁店/高端展厅实景)",
        "delay_days": 4,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

One detail that might give you confidence:

One of our overseas partners won and supplied the lighting for NIKE retail stores across more than 10 states with over 6,000 units of our zoomable architectural fixtures, strictly complying with visual comfort and strict maintenance standards.

In addition, our modular components allow 7-day fast dispatch for project prototypes.

Happy to share our full project case study video and IES files if you are reviewing fittings for current jobs.

Best regards,

Bob | Encore Commercial Lighting"""
    },
    {
        "step_number": 4,
        "step_name": "Step 4: 礼貌收尾 Break-up (转介绍与关闭沟通)",
        "delay_days": 7,
        "is_thread_reply": 1,
        "subject": "Re: {subject_step1}",
        "body_template": """Hi {first_name},

I haven't heard back, so I assume you either have fully satisfied suppliers in place or your hands are full with project delivery. I'll stop following up to keep your inbox clean.

If you are not the right person for lighting specifications at {company}, could you kindly refer me to who manages your fixture sourcing?

Whenever you need reliable architectural samples in the future, my email is always open.

Wishing you and the {company} team continued success!

Best regards,

Bob | Encore Commercial Lighting"""
    }
]

# 精选买家库：严格锁定今天的 19 家真实买家 (英国第三轮 3 家 + 中东阿联酋 9 家 + 中东沙特 7 家)
from sync_today_leads import TODAY_LEADS as ENCORE_LEADS
