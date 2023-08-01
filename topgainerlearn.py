import requests
import slugify
from bs4 import BeautifulSoup
page_to_scrape=requests.get('https://www.sharesansar.com/top-gainers')
soup=BeautifulSoup(page_to_scrape.text,"html.parser")

def parse_columns(self,soup: BeautifulSoup) -> list:
        t_heads = soup.find_all("thead")
        columns = []
        for t_head in t_heads:
            for th in t_head.find_all("th"):
                th = th.text.replace("%", "percent")
                column = slugify(th)
                column = column.replace("-", "_")
                if not column.isidentifier():
                    column = "_" + column
                columns.append(column)
        return columns

def parse_data(self, soup: BeautifulSoup):
        columns = self.parse_columns(soup)
        print(columns)


def update_today_price(self):
        soup = self.fetch_data()
        today_prices = self.parse_data(soup)
        return today_prices


        # today_prices = self.parse_rows(soup, columns)
        # df = self.format_data(today_prices)
        # today_prices = df.to_dict(orient="records")
        # self.save_as_json(FILE_NAME, today_prices)
        # return today_prices

# columns = self.parse_columns(soup)
# t_heads = soup.find_all("table")
# print(t_heads)
# columns = []
# for t_head in t_heads:
#     for th in t_head.find_all("th"):
#         th = th.text.replace("%", "percent")
#         column = slugify(th)
#         column = column.replace("-", "_")
#         if not column.isidentifier():
#             column = "_" + column
#             columns.append(column)
    # 
# print(columns)