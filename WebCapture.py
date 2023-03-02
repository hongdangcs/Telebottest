from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the page
driver.get("https://www.tradingview.com/chart/?symbol=HOSE%3AVNINDEX")
"""
element = driver.find_element(By.CLASS_NAME, 'credential_picker_container')
driver.execute_script("arguments[0].remove()", element)


element = driver.find_element(By.CLASS_NAME, 'container-Uxy01IQ6')
driver.execute_script("arguments[0].remove()", element)
element = driver.find_element(By.CLASS_NAME, 'backdrop-Uxy01IQ6')
driver.execute_script("arguments[0].remove()", element)
"""
#element = driver.find_element_by_xpath("//div[@class='k1zIA rSk4se']")

element = driver.find_element(By.CLASS_NAME, 'chart-container')

# Capture a screenshot and save it to a file
element.screenshot("C://Users//PHAMHONGDANG//Downloads//ScreenShot//MakeSc.png")

# Close the driver
driver.quit()