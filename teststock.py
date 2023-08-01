import requests
from bs4 import BeautifulSoup


r=requests.get("https://www.sharesansar.com/top-gainers")
c=r.content
soup = BeautifulSoup(c, "html.parser")
table =soup.findAll("table", {"id": "myTable"})
table_rows = soup.findAll("thead")
tr1=soup.findAll("tr",{"role":"row"})
print(tr1)
print(table_rows)


for tr in table_rows:
 td = tr.find_all("td")
 row = [i.text for i in td]
 print(row)