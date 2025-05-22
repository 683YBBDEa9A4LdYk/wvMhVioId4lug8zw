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
    print("Bulunan M3U8 URL'si:", m3u8_url)

    # URL'yi test et
    test_response = requests.get(m3u8_url, headers=headers)
    if test_response.status_code == 200:
        print("M3U8 başarıyla çalışıyor!")

        # M3U8 içeriğini dosyaya yaz
        with open("now.m3u8", "wb") as f:
            f.write(test_response.content)
        print("M3U8 dosyası başarıyla 'now.m3u8' olarak kaydedildi!")
    else:
        print(f"M3U8 çalışmıyor. Status Code: {test_response.status_code}")
else:
    print("daiUrl bulunamadı!")
