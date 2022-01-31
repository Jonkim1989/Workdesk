import requests
from bs4 import BeautifulSoup



url = "https://www.google.com/search?q=%ED%8C%8C%EC%9D%B4%EC%8D%AC&rlz=1C1PNBB_enKR982KR982&oq=%ED%8C%8C%EC%9D%B4%EC%8D%AC&aqs=chrome.0.69i59l4j69i65j69i60l3.1286j0j7&sourceid=chrome&ie=UTF-8"
# headers를 적용하면 정보를 가졍올 수 없다고 함, 

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# url 정보를 html 문서로 저장하기 (매번 하지 않도록 완성시 주석 처리하기)
with open("google_sample.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

# 가져온 url 정보 중 필요한 내용만 찾아내기 (실제 구글에서는 class명이 다르다. = LC20lb MBeuO DKV0Md)
data_rows = soup.find_all("div", attrs={"class":"BNeawe vvjwJb AP7Wnd"}) 

# link = soup.find_all("a", attrs=["href"])


for idx, data in enumerate(data_rows):
    print(f"{idx+1}위", data.get_text())


