from urllib.parse import quote_plus # 한글을 검색창에 맞는 특수문자로 변환 시켜줌
from bs4 import BeautifulSoup
from selenium import webdriver

Keyword = "파이썬"

for i in range(0, 3):
    url = "https://www.google.com/search?q=" + quote_plus(Keyword) + f"&start={i}0" # PlusUrl 에 한글 자동변환 파서 적용

    driver = webdriver.Chrome()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html)

    r = soup.select(".tF2Cxc")

    for idx, data in enumerate(r):
        print(f"{i+1}페이지 {idx+1}위")
        print(data.select_one(".LC20lb.MBeuO.DKV0Md").text) # 타이틀 가져오기
        # print(i.select_one(".iUh30.qLRx3b.tjvcx").text) # 경로 가져오기
        print(data.a.attrs["href"])
        print()
