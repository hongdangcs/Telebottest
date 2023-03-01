from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the page
driver.get("https://google.com")

#element = driver.find_element_by_xpath("//div[@class='k1zIA rSk4se']")

element = driver.find_element(By.CLASS_NAME, 'om7nvf')

# Capture a screenshot and save it to a file
element.screenshot("C://Users//PHAMHONGDANG//Downloads//ScreenShot//screenshotelement.png")

# Close the driver
driver.quit()