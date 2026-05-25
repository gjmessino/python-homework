import pandas as pd
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://owasp.org/Top10/2025/')
    sleep(2) # wait 2 seconds
    driver.get('https://owasp.org/Top10/2025/')
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

vuls = driver.find_elements(By.XPATH, '//ol/li')
results = []
for items in vuls:
    print(items.text)
    results.append(items.text)

df = pd.DataFrame(results)

df.to_csv('./owasp_top_10.csv')