import datetime
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}

Moneysite = "https://onlinecasino79.com/".replace("https://", "").replace(
    "http://", "").replace("www.", "").replace("/", "")
Keywords = "카지노사이트, 바카라사이트, 블랙잭사이트, 룰렛사이트".split(", ")
Ranking = []
Date_now = datetime.date.today()

print()
print(f"{Moneysite}검색 시작")
print("Google 검색일자: " + f"{Date_now}")

for Keyword in Keywords:
    for page_num in range(0, 100):
        url = f"https://www.google.com/search?q={Keyword}&start={page_num}0"

        res = requests.get(url, headers=hdr)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        # url 정보를 html 문서로 저장하기 (매번 하지 않도록 완성시 주석 처리하기)
        # with open("google_sample.html", "w", encoding="utf8") as f:
        #     f.write(soup.prettify())

        # 가져온 url 정보 중 필요한 내용만 찾아내기
        data_rows = soup.find_all("div", attrs={"class": "yuRUbf"})
        next_button = soup.find("a", attrs={"id": "pnnext"})

        for idx, data in enumerate(data_rows):
            # 루트 도메인만 추출해서 페이지와 순위 표시
            # 도메인만 추출 후 타겟 url과 일치하면 기록하기
            target_url = urlparse(
                data.find("a")["href"]).netloc.replace("www.", "")
            if target_url == Moneysite:
                Ranking.append(f"{Keyword}: {page_num+1}페이지 {idx+1}위")
                print(f"{Keyword}: {page_num+1}페이지 {idx+1}위")
                break
            else:
                continue

        # 다음 페이지 버튼이 있으면 계속 진행, 없으면 빠져나오기
        if target_url == Moneysite:
            break

        if next_button:
            continue
        else:
            print(f"{Keyword}: - (~{page_num+1})")
            Ranking.append(f"{Keyword}: -")
            break


print()
print("검색 결과")
print()
print("Google 검색일자: " + f"{Date_now}")
print()
for i in Ranking:
    print(i)


# request 로 각 페이지마다 사이트 순위를 출력하기까지 완료.
# 이걸 CVS 로 정리하고 키워드를 가져와서 검색후 노출 중인 순위를 다시 CVS 로 저장 시키기
# 이제 엑셀 다루는 강의를 들어야겠다
