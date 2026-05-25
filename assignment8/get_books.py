# Imports
import pandas as pd
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Creating Driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Letting driver get webpage
try:
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
    sleep(2) # wait 2 seconds
    driver.get('https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart')
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")

#Task 3
book_list = driver.find_elements(By.CSS_SELECTOR, 'li.cp-search-results-item')
results = []

#iterate through books
if (book_list):
    for book in book_list:
        title = book.find_element(By.CSS_SELECTOR, 'h3[class= cp-title]')
        print(title)
        author = book.find_element(By.CSS_SELECTOR, 'a[class= author-link]')
        info_div = book.find_element(By.CSS_SELECTOR, 'div[class= cp-format-info]')
        info_text = info_div.find_element(By.CSS_SELECTOR, 'span [class = display-info-primary]')
        dict_entry = {'Title' : title,
                      'Author' : author,
                      'Format-Year': info_text}
        results.append(dict_entry)

df = pd.DataFrame(results)

#Task 4
df.to_csv('./get_books.csv')
df.to_json('get_books.json', orient='records', indent=2)

driver.quit()