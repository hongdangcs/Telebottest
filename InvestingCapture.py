from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize the driver
def investCapture(imageName, domainName):
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Navigate to the page
    driver.get("https://www.tradingview.com/chart/?symbol="+domainName)

    # element = driver.find_element_by_xpath("//div[@class='k1zIA rSk4se']")

    element = driver.find_element(By.CLASS_NAME, 'isFirst-Jc9IXW74')
    element.click()
    time.sleep(1.5)
    element = driver.find_element(By.CLASS_NAME, 'chart-container')

    # Capture a screenshot and save it to a file
    element.screenshot("C://Users//PHAMHONGDANG//Downloads//ScreenShot//"+imageName+".png")

    element = driver.find_element(By.CLASS_NAME, 'price-qqt8UV2f')
    content = element.text

    element = driver.find_element(By.CLASS_NAME, 'currency-qqt8UV2f')
    content = content + element.text

    driver.quit()
    return content


# Close the driver
