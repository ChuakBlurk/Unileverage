import imp
from multiprocessing.sharedctypes import Value
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
from utils import closeDialog, scrollDown


def readAnswerList(browser):
    answer_element_list = browser.find_elements(by = By.XPATH, value = "//div[@class='RichContent-inner']")
    answer_list = []
    for answer_item in answer_element_list:
        answer_list.append(answer_item.text)
    return answer_list
        
def fetchAnswersOfQuestion(qid):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)     
    browser.get("https://www.zhihu.com/question/" + str(qid))
    # close the floating window
    closeDialog(browser, "//button[@aria-label='关闭']")
    scrollDown(browser, 1)
    print(readAnswerList(browser))
    time.sleep(600)


if __name__ == "__main__":
    qid = "412349836"
    fetchAnswersOfQuestion(qid)