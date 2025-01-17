import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

exchangeList = soup.select("#exchangeList > li")

exchange_datas = []
baseUrl = "https://finance.naver.com"

for item in exchangeList:
    data = {
        "title": item.select_one(".h_lst").text,
        "exchange": item.select_one(".value").text,
        "change": item.select_one(".change").text,
        "updown": item.select_one("div.head_info.point_dn > .blind").text,
        "link": baseUrl + item.select_one("a").get("href")
    }
    exchange_datas.append(data)
exchange_datas
df = pd.DataFrame(exchange_datas)
df.to_excel("./naverfinance.xlsx")