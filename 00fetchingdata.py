import requests

def FetchAndSaceToFile(url,path):
    r = requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city"
# r = requests.get(url)
# print(r.text)
FetchAndSaceToFile(url,"data/times.html")