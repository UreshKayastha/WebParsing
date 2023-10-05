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
service=ChromeService
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

rows=driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
rows_count=len(rows)
columns=driver.find_elements(By.XPATH,"//table[@id='table1']//th")
column_count= len(columns)
print(column_count)

for r in range(1, rows_count+1):
    for c in range(1,column_count+1):
        if r==1:
            data=driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r)+"]//th["+str(c)+"]")
            # print(data.text)
        else:
            # data=driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r-1)+"]//td["+str(c)+"]")
            # data=driver.find_element(By.XPATH,"//table[@id='table1']/tbody//tr["+str(r-1)+"]//td["+str(c)+"]")
            data=driver.find_element(By.XPATH,"//*[@id='table1']/tbody/tr["+str(r-1)+"]/td["+str(c)+"]")
            print(data.text)
# //*[@id="table1"]/tbody/tr[3]/td[1]
# //*[@id="table1"]/tbody/tr[2]/td[1]
driver.quit()