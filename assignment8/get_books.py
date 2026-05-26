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
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
    sleep(2) # wait 2 seconds
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

li_lists = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-result-item')
print(len(li_lists))

results = []
for entry in li_lists:
    title = entry.find_element(By.CSS_SELECTOR, 'h3.cp-title')
    author_list = []
    author_entry = entry.find_elements(By.CSS_SELECTOR, 'a.author-link')
    for auth in author_entry:
        author_list.append(auth.text)
    author = " ;".join(author_list)
    year = entry.find_element(By.CSS_SELECTOR, 'span.display-info-primary')
    dict_entry = {'Title' : title.text,
                  'Author' : author,
                  'Format-Year': year.text}
    results.append(dict_entry)

df = pd.DataFrame(results)
print(df)

df.to_csv('./get_books.csv')
df.to_json('./get_books.json')

driver.quit()