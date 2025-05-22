import requests
import re

url = "https://www.nowtv.com.tr/canli-yayin"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Sayfayı çek
response = requests.get(url, headers=headers)
html_content = response.text

# daiUrl'yi regex ile bul
pattern = r"daiUrl\s*:\s*'([^']+\.m3u8[^']*)'"
match = re.search(pattern, html_content)

if match:
    m3u8_url = match.group(1)

    # m3u8_url'yi dosyaya yaz
    with open("nowtv.m3u8", "w") as file:
        file.write(m3u8_url)
