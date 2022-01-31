# 나도 코딩 따라서 작성한 코드

from urllib.parse import quote_plus # 한글을 검색창에 맞는 특수문자로 변환 시켜줌
from bs4 import BeautifulSoup
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("naver.com")


