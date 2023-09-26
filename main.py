from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time
import pdb


#open chrome from cmd using below code
#"C:\Users\jainprs\AppData\Local\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"


driver_path = r"C:\Users\jainprs\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(service=service, options=chrome_options)
# print(driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")

box = soup.find_all("div", class_ = "sc-gdJbiX dAPPgT search-result-in-panel")
for i in box:
    name = i.find("div", class_ = "sc-hitSbr bOsRyq").text.strip()
    addr = i.find("p", class_ = "undefined adr").text.strip()
    phone = i.find("a", class_ = "phone").text.strip().split("phonefor")[0]
    print(phone)

