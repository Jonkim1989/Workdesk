import requests

proxies = "https":"https://164.100.130.128:8080"

r = requests.get("https://ipinfo.io/json", proxies=proxies)

print(r.json.text)