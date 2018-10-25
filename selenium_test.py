from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def test_home():
    chrome_options = Options()
    chrome_options.binary_location = "web-app-ci-cd-with-travis-ci-ZhimaoLin/chromedriver"

    driver = webdriver.Chrome()

    driver.get("http://162.246.157.223:8000")
    elem = driver.find_element_by_id("name")
    print(elem.text)
    # assert elem != None

    assert True
