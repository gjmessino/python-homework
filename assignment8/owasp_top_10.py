import pandas as pd
import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://owasp.org/www-project-top-ten/')
    ... # extract data
    sleep(2) # wait 2 seconds
    driver.get('https://owasp.org/www-project-top-ten/')
except Exception as e:
    print(f"An exception occurred: {type(e).__name__} {e}")
finally:
    driver.quit()