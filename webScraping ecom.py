
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

r=requests.get("https://api64.ipify.org?format=json")
print(r.json())

ua = UserAgent()
print(ua.chrome)
headers = {'User-Agent':str(ua.chrome)}
print(headers)

data ={"title":[],"price":[]}

url = "https://www.amazon.in/s?k=iphone&crid=37IS9ATGGUJLS&sprefix=iphone%2Caps%2C258&ref=nb_sb_noss_1"
r = requests.get(url,headers=headers)
soup=BeautifulSoup(r.text,"html.parser")
# print(soup.prettify())

spans=soup.find(class_="rush-component")
print(spans)

spans=soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices=soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
         print(price.find("span").get_text())
         data["price"].append(price.find("span").get_text())
         if len(data["price"])==len(data["title"]):
            break

df= pd.DataFrame.from_dict(data)
df.to_csv("Data.csv",index=False)


