import json
from urllib.parse import urljoin

import pandas as pd
import requests
from bs4 import BeautifulSoup
from slugify import slugify


FILE_NAME = "today_prices.json"
BASE_URL = "https://www.sharesansar.com/"
TODAY_PRICE_URL = "today-share-price"

def update_today_price(self):
        soup = self.fetch_data()
        today_prices = self.parse_data(soup)
        return today_prices
def fetch_data(self) -> BeautifulSoup:
        url = urljoin(self.base_url, TODAY_PRICE_URL)
        response = self.fetch_response(url)
        soup = BeautifulSoup(response, "html.parser")
        print(soup)
        return soup

update_today_price()