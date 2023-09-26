from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time


# Specify the path to the Chrome WebDriver executable
driver_path = r"C:\Users\iampr\Downloads\chromedriver-win64\chromedriver.exe"
service = Service(driver_path)


# Configure Chrome options to connect to an existing browser using remote debugging
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Create a Chrome WebDriver instance with the specified service and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Initialize an empty BeautifulSoup object to store the combined HTML content
soup = BeautifulSoup("", "html.parser")


page_count = 0


while page_count < 7:
    time.sleep(5)
    try:
        # Get the HTML content of the current page
        current_page_html = driver.page_source
        time.sleep(5)

        # Parse the HTML content of the current page using BeautifulSoup
        current_page_soup = BeautifulSoup(current_page_html, "html.parser")
        time.sleep(5)

        # Append the HTML content of the current page to the combined HTML
        soup.append(current_page_soup)
        time.sleep(5)

        # Find and click the "Next" button
        next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[1]/div/div/div[3]/herc-product-list-page/div/div[2]/div[2]/div[3]/div[8]")))
        next_btn.click()
        print(page_count)
        page_count += 1
        time.sleep(15)
        
       
    
    except Exception as e:
        print("No more 'Next' button found. Exiting the loop.")
        break


#creating a box from soup which contains html of all pages
box = soup.find_all("div", class_="product-container")

product_titles = []
product_descriptions = []
prices_day = []
prices_week = []
prices_month = []


for i in box:
    product_title = i.find("a", class_="product-details-title").text.strip()
    product_description = "\n".join([li.text.strip() for li in i.find("div", class_="product-details-description").find_all("li")])
    pricing = [div.text.strip() for div in i.find("div", class_="product-pricing-description").find_all("div")]

    product_titles.append(product_title)
    product_descriptions.append(product_description)
    prices_day.append(pricing[0])
    prices_week.append(pricing[1])
    prices_month.append(pricing[2])


data = {
    "Product Title": product_titles,
    "Product Description": product_descriptions,
    "Price /day": prices_day,
    "Price /week": prices_week,
    "Price /month": prices_month
}

df = pd.DataFrame(data)
print(df)

df.to_csv("herc_rentals.csv", index=False)