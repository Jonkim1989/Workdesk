import datetime
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

url = "https://www.creamtk.net/"

res = requests.get(url, headers=hdr)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# url 정보를 html 문서로 저장하기 (매번 하지 않도록 완성시 주석 처리하기)
with open("creamtk_net.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

