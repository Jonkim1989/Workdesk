# 한글 키워드 검색시 문제가 발생할 경우 참고할 코드
# https://www.youtube.com/watch?v=3b_VMk3WlNY - 유튜브 참고




import urllib.request
from urllib.parse import quote_plus # 한글을 검색창에 맞는 특수문자로 변환 시켜줌
from bs4 import BeautifulSoup


hdr = {'User-Agent': 'Mozilla/5.0'}
baseUrl = "https://www.google.com/search?q="
keyword = "파이썬"
url = baseUrl + quote_plus(keyword) # PlusUrl 에 한글 자동변환 파서 적용

res = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(res).read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# url 정보를 html 문서로 저장하기 (매번 하지 않도록 완성시 주석 처리하기)
with open("google_sample.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

row_data = soup.find_all("div", attrs={"id":"main"})

url_list = []

for i in row_data:
    url_list.append((i.a["href"]).replace("/url?q=", "")) # http 앞 부분 제외

print(len(url_list))

for i in url_list:
    print(i)


