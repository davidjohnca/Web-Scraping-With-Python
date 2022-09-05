#IMPORT NECESSARY LIBRARIES

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# CREATE URL GETTER
driver = webdriver.Chrome('/Users/David/OneDrive - IFPI/Desktop/my_python_files/chromedriver')
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')

# CLOSING POP UP WINDOW
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="at-cv-lightbox-close"]').click()

# ENTERING A MESSAGE
driver.find_element(By.XPATH, '//*[@id="user-message"]').send_keys('Hello World')
driver.find_element(By.XPATH, '//*[@id="get-input"]/button').click()

# COMPUTING A SUM
driver.find_element(By.XPATH, '//*[@id="sum1"]').send_keys('10')
driver.find_element(By.XPATH, '//*[@id="sum2"]').send_keys('11')
driver.find_element(By.XPATH, '//*[@id="gettotal"]/button').click()