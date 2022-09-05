# IMPORT NECESSARY LIBRARIES

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# CREATE URL GETTER
driver = webdriver.Chrome('/Users/David/OneDrive - IFPI/Desktop/my_python_files/chromedriver')
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# ISOLATE DESIRED ELEMENTS
source = driver.find_element(By.XPATH, '//*[@id="box3"]')
destination = driver.find_element(By.XPATH, '//*[@id="box103"]')

# SPECIFY THE ACTION, IN THIS CASE DRAG AND DROP
actions = ActionChains(driver)
actions.drag_and_drop(source, destination).perform()