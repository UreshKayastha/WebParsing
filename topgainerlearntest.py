import requests
import slugify
from bs4 import BeautifulSoup
data=requests.get('https://www.sharesansar.com/top-gainers')
data = data.content

response = data
soup = BeautifulSoup(response, "html.parser")
t_heads = soup.find_all("div")
print(t_heads)

# t_heads = soup.findAll("thead",attrs={"class":"bg-danger"})
# t_rows=soup.find_all("th",attrs={"class":"sorting_disabled"})
# print(t_rows.style)
