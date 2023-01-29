from bs4 import BeautifulSoup
from urllib.request import urlopen


# 위키피디아 메인페이지 파싱하기
# response = urlopen("https://en.wikipedia.org/wiki/main_page")
# soup = BeautifulSoup(response, "html.parser")
# for anchor in soup.find_all("a"):
#     print(anchor.get("href", "/"))


# 네이버 순위 파싱하기
response = urlopen("https://www.naver.com/")
soup = BeautifulSoup(response, "html.parser")
for anchor in soup.select("strong.title"):
    print(anchor)