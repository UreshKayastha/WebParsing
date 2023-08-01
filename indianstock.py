import requests
from bs4 import BeautifulSoup


r = requests.get("https://finviz.com")
soup = BeautifulSoup(r.content, "html.parser")


for table in soup.find_all("table", {"class": "t-home-table"}):
    print()

    for tr in table.find_all("tr"):
        td = tr.find_all("td")
        row = [i.text for i in td]

        if len(row) > 5 and row[5] in ['Top Gainers', 'Top Losers']:
            print(row)