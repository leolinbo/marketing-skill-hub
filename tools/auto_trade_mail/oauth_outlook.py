# -*- coding: utf-8 -*-
"""
Microsoft Outlook OAuth 2.0 (XOAUTH2) 认证模块
支持标准 OAuth 2.0 授权码置换与 Token 自动续期
"""
import time
import base64
import urllib.parse
import urllib.request
import json
from typing import Dict, Any, Tuple

OAUTH_AUTH_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/authorize"
OAUTH_TOKEN_URL = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
OAUTH_SCOPES = "offline_access https://outlook.office.com/SMTP.Send User.Read"

def build_authorization_url(client_id: str, redirect_uri: str) -> str:
    """构建前往微软的登录授权跳转链接"""
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "response_mode": "query",
        "scope": OAUTH_SCOPES,
        "state": "outlook_setup"
    }
    return f"{OAUTH_AUTH_URL}?{urllib.parse.urlencode(params)}"

def exchange_code_for_token(client_id: str, client_secret: str, redirect_uri: str, code: str) -> Dict[str, Any]:
    """使用授权码 code 换取 Access Token 与 Refresh Token"""
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri,
        "scope": OAUTH_SCOPES
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(OAUTH_TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(req, timeout=15) as resp:
        res_json = json.loads(resp.read().decode("utf-8"))
        return res_json

def refresh_access_token(client_id: str, client_secret: str, refresh_token: str) -> Tuple[str, int]:
    """使用 Refresh Token 静默续期 Access Token"""
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "refresh_token": refresh_token,
        "grant_type": "refresh_token",
        "scope": OAUTH_SCOPES
    }
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(OAUTH_TOKEN_URL, data=data, method="POST")
    req.add_header("Content-Type", "application/x-www-form-urlencoded")

    with urllib.request.urlopen(req, timeout=15) as resp:
        res_json = json.loads(resp.read().decode("utf-8"))
        access_token = res_json.get("access_token", "")
        expires_in = int(res_json.get("expires_in", 3600))
        return access_token, expires_in

def generate_xoauth2_string(user: str, token: str) -> str:
    """生成 SASL XOAUTH2 认证字符串并进行 Base64 编码"""
    auth_str = f"user={user}\x01auth=Bearer {token}\x01\x01"
    return base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
