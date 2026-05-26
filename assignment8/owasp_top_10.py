import json
import csv
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://owasp.org/www-project-top-ten/')
    sleep(2) # wait 2 seconds
    driver.get('https://owasp.org/www-project-top-ten/')
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

first_page = driver.find_element(By.XPATH, '//*[@id="sec-main"]/p[1]/a')
url = first_page.get_attribute('href')
driver.get(url)

vuls = driver.find_elements(By.XPATH, '//ol/li')
results = []
for items in vuls:
    title = items.text
    a_select = items.find_element(By.CSS_SELECTOR, 'a')
    link = a_select.get_attribute('href')
    my_dict = {"Title" : title,
               "Link": link}
    results.append(my_dict)

df = pd.DataFrame(results)
df.to_csv('./owasp_top_10.csv')

driver.quit()