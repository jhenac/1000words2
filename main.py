from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

language = input(f"What would you like to learn?: ").lower()
url = f"https://1000mostcommonwords.com/1000-most-common-{language}-words/"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(url)

data = []
tables = driver.find_elements(By.CSS_SELECTOR, "table")
with open(f"{language}_words.csv", "w", newline='') as f:
    writer = csv.writer(f)
    for n in range(len(tables)):
        for row in tables[n].find_elements(By.CSS_SELECTOR, "tr"):
            writer.writerow([d.text for d in row.find_elements(By.CSS_SELECTOR, "td")])



