from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def closeDialog(webdriver, xpath_value):
    elements = webdriver.find_element(by = By.XPATH, value = xpath_value)
    elements.click()
    time.sleep(2)
    
    
def scrollDown(webdriver, scroll_pause_time):
    # Get scroll height
    last_height = webdriver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = webdriver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(2)
