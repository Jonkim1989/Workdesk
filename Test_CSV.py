import csv
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

filename = "검색순위기록.csv"

f = open(filename, "w", encoding="utf-8-sig", newline="")
wr = csv.writer(f)
# wr.writerow({1,2,3})
wr.writerows([[1,2,3],[4,5,6],[7,8,9]])
f.close()

