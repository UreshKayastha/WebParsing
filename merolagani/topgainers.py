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
driver.get("https://merolagani.com/MarketSummary.aspx?type=gainers")
time.sleep(1.4)
matches=driver.find_elements(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr")

matches_body=driver.find_elements(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody")

Symbol=[]
LTP=[]
Per_Change=[]
High=[]
Low=[]
Open=[]
Qty=[]
Turnover=[]
# /html/body/form/div[4]/div[3]/div/div/table/tbody/tr[2]/td[1]/a
# //*[@id="ctl00_ContentPlaceHolder1_tblSummary"]/tbody/tr[2]
# print(matches_body)
print(len(matches))
print(len(matches_body))

for i in range(2,20):
    Symbol.append(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[1]").text)
    # Symbol.append(matches_body.find_element(By.XPATH,"./tr["+str(i)+"]/td[1]").text)
    LTP.append(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[2]").text)
    Per_Change.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[3]").text))
    High.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[4]").text))
    Low.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[5]").text))
    Open.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[6]").text))
    Qty.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[7]").text))
    Turnover.append(float(driver.find_element(By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_tblSummary']/tbody/tr["+str(i)+"]/td[8]").text))
    # result_value=""
    # for alphabet in original_value:
    #     if alphabet !=",":
    #         result_value=result_value+alphabet
    # value.append(float(result_value))
    # value.append(float(k.find_element(By.XPATH,'./td[4]').text))
    # Point_Change.append(float(k.find_element(By.XPATH,'./td[5]').text))
    # Per_ChangeD.append(float(k.find_element(By.XPATH,'./td[6]').text))
    # Per_Change.append(float(k.find_element(By.XPATH,'./td[6]').text))
    

# print(Symbol.text)
    # abc=k.text 
    # print(abc)

    # df = pd.read_csv(k.text, sep='\s+')
    # df.to_csv('my_file.csv', header=None)

# df.to_json('topgainers1.json')

# //*[@id="myTable"]/tbody/tr[1]/td[1]
# df=pd.DataFrame({'Symbol':Symbol,'LTP':LTP,'Per_Change':Per_Change,'High':High,'Low':Low,'Open':Open,'Qty':Qty,'Turnover':Turnover})
df=pd.DataFrame({'Symbol':Symbol,'LTP':LTP})
# df.to_csv('top_gainers.csv',index=False)
# df=pd.DataFrame(data)
print(df)
dfObjects=df.to_dict("records")

with open('merolaganitop_gainers.json', "w") as f:
    json.dump(dfObjects, f, indent=2)

driver.quit()
