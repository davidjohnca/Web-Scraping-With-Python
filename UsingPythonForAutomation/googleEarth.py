# IMPORT NECESSARY LIBRARIES

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CREATE URL GETTER
driver = webdriver.Chrome('/Users/David/OneDrive - IFPI/Desktop/my_python_files/chromedriver')
driver.maximize_window()
driver.get('https://www.google.com/earth/index.html')

# TELL THE PROGRAM TO WAIT 10 SECONDS BEFORE CLICKING ON THE LUNCH EARTH BUTTON
wait = WebDriverWait(driver, 10)
launch_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launch_button.click()