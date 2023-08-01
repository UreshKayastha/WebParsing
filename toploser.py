from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
import pandas as pd
import json
import time
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# service = ChromeService(executable_path="C:/Users/SnappFood/.cache/selenium/chromedriver/win32/110.0.5481.77/chromedriver.exe")
service=ChromeService


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.sharesansar.com/top-losers")
matches=driver.find_elements(By.XPATH,'//*[@id="myTable"]/thead/tr/th')
matches_body=driver.find_elements(By.XPATH,'//*[@id="myTable"]/tbody/tr')
sn=[]
symbol=[]
name=[]
value=[]
Point_Change=[]
Per_Change=[]

# for j in matches:
#     a=j.find_element(By.XPATH,'//*[@id="myTable"]/thead/tr/th[2]').text
#     print(a)

for k in matches_body:
    sn.append(k.find_element(By.XPATH,'./td[1]').text)
    symbol.append(k.find_element(By.XPATH,'./td[2]').text)
    name.append(k.find_element(By.XPATH,'./td[3]').text)
    original_value=k.find_element(By.XPATH,'./td[4]').text
    result_value=""
    for alphabet in original_value:
        if alphabet !=",":
            result_value=result_value+alphabet
    value.append(float(result_value))
    original_change=k.find_element(By.XPATH,'./td[5]').text
    result_change=""
    for alphabet in original_change:
        if alphabet !=",":
            result_change=result_change+alphabet
    Point_Change.append(float(result_change))
    
    # value.append(float(k.find_element(By.XPATH,'./td[4]').text))
    # Point_Change.append(float(k.find_element(By.XPATH,'./td[5]').text))
    Per_Change.append(float(k.find_element(By.XPATH,'./td[6]').text))
    

# //*[@id="myTable"]/tbody/tr[1]/td[1]
df=pd.DataFrame({'SN':sn,'symbol':symbol,'Name':name,'LTP':value,'Point_Change':Point_Change,'Per_Change':Per_Change})
# df.to_csv('top_gainers.csv',index=False)
# print(df)
dfObjects=df.to_dict("records")

with open('top_losers.json', "w") as f:
    json.dump(dfObjects, f, indent=2)

driver.quit()
