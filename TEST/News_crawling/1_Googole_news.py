import requests
from bs4 import BeautifulSoup

hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
def create_soup(url):
    res = requests.get(url, headers=hdr)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    
    # 흐림, 어제보다 00도 높아요 
    cast = soup.find("p", attrs={"class":"summary"}).get_text()
    # 현재 00도 
    curr_temp = soup.find("div", attrs={"class":"temperature_text"}).get_text().strip()
    moist_temp1 = soup.find_all("dt", attrs={"class":"term"})
    moist_temp2 = soup.find_all("dd", attrs={"class":"desc"})
    dust_lvl = soup.find("li", attrs={"class":"item_today level1"}).get_text().strip()
    

    print(cast)
    print(curr_temp)
    print(f"{moist_temp1[1].get_text()} {moist_temp2[1].get_text()}")
    print(dust_lvl)

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/"
    soup = create_soup(url)

    # 왼쪽 헤드라인 뉴스 가져오기
    H_news_hrefs = soup.find_all("div", attrs={"class":"cjs_journal_wrap _item_contents"}, limit=3)
    for index, news in enumerate(H_news_hrefs):
        link = news.find("a")["href"]
        title = news.find("a").get_text().strip()
        
        
        print(title)
        print(link)
        print()






if __name__ == "__main__":
    # scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 네이버 헤드라인 뉴스 가져오기
