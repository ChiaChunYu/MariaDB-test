import selenium
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import mysql.connector
import re

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="411021390",
  database="newdatabase"
)

mycursor = mydb.cursor()

stock_code = "2330"
driver = webdriver.Chrome()
driver.get("https://tw.stock.yahoo.com/") 
driver.maximize_window()
driver.find_element(By.ID, "ssb-search-input").send_keys(stock_code)
time.sleep(2)
driver.find_element(By.ID, "ssb-search-input").send_keys(Keys.ENTER)
driver.find_element(By.XPATH, '//*[@id="main-1-QuoteTabs-Proxy"]/nav/div/div/div[9]/a/span/div/span').click()
time.sleep(2)
element = driver.find_element(By.XPATH, '//*[@id="main-2-QuoteProfile-Proxy"]/div/section[3]/div[2]')
text = element.text
cleaned_text = re.sub(r'[^\w]', '_', text)
print(text)
print(cleaned_text)
element = driver.find_element(By.XPATH, '//*[@id="main-2-QuoteProfile-Proxy"]/div/section[3]/div[3]/div[1]/div/div')
gross_profit_margin = element.text
print('營業毛利率:',gross_profit_margin)
element = driver.find_element(By.XPATH, '//*[@id="main-2-QuoteProfile-Proxy"]/div/section[3]/div[3]/div[3]/div/div')
operating_profit_margin = element.text
print('營業利益率:',operating_profit_margin)
element = driver.find_element(By.XPATH, '//*[@id="main-2-QuoteProfile-Proxy"]/div/section[3]/div[3]/div[5]/div/div')
pretax_profit_margin = element.text
print('稅前淨利率:',pretax_profit_margin)  



# 創建表格
try:
    mycursor.execute(f"CREATE TABLE {cleaned_text} (id INT AUTO_INCREMENT PRIMARY KEY, stock_code VARCHAR(255), gross_profit_margin VARCHAR(255), operating_profit_margin VARCHAR(255), pretax_profit_margin VARCHAR(255))")
    print("Table created successfully")
except mysql.connector.Error as err:
    print(f"Failed to create table: {err}")

# 插入資料
try:
    mycursor.execute(f"SELECT * FROM {cleaned_text} WHERE stock_code = %s", (stock_code,))
    result = mycursor.fetchall()
    if len(result) == 0:
        sql = f"INSERT INTO {cleaned_text} (stock_code, gross_profit_margin, operating_profit_margin, pretax_profit_margin) VALUES (%s, %s, %s, %s)"
        val = (stock_code, gross_profit_margin, operating_profit_margin, pretax_profit_margin)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    else:
        print("Record already exists.")
except mysql.connector.Error as err:
    print(f"Failed to insert record: {err}")

# 關閉連線
mydb.close()