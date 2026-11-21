import urllib.request
import json

url = "https://www.instagram.com/api/v1/users/web_profile_info/?username=rar_aguiar"
req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-ig-app-id": "936619743392459",
        "Accept": "*/*"
    }
)

try:
    with urllib.request.urlopen(req, timeout=10) as response:
        data = json.loads(response.read().decode('utf-8'))
        user = data.get('data', {}).get('user', {})
        print("Username:", user.get('username'))
        print("Full Name:", user.get('full_name'))
        print("Biography:", user.get('biography'))
        print("Category:", user.get('category_name'))
        print("External URL:", user.get('external_url'))
        print("Followers:", user.get('edge_followed_by', {}).get('count'))
        print("Following:", user.get('edge_follow', {}).get('count'))
        print("Is Business:", user.get('is_business_account'))
        print("Is Professional:", user.get('is_professional_account'))
except Exception as e:
    print("Error:", e)
