from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Initialize the driver
def investCapture(imageName, domainName):


    #driver = webdriver.Chrome()
    #driver.maximize_window()

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    # Initialize the WebDriver with the options
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    # Navigate to the page
    driver.get("https://www.tradingview.com/chart/?symbol="+domainName)

    # element = driver.find_element_by_xpath("//div[@class='k1zIA rSk4se']")
    driver.save_screenshot("photo/"+imageName+".png")

    #element = driver.find_element(By.CLASS_NAME, 'price-qqt8UV2f')

    driver.quit()
    return " price "
"""
    element = driver.find_element(By.CLASS_NAME, 'isFirst-Jc9IXW74')
    element.click()
    time.sleep(1.5)
    element = driver.find_element(By.CLASS_NAME, 'chart-container')

    # Capture a screenshot and save it to a file
    element.screenshot("photo/"+imageName+".png")

    element = driver.find_element(By.CLASS_NAME, 'price-qqt8UV2f')
    content = element.text

    element = driver.find_element(By.CLASS_NAME, 'currency-qqt8UV2f')
    content = content + element.text
"""


# Close the driver
