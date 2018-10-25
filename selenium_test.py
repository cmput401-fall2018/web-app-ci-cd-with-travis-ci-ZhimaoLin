from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def test_home():
    chrome_options = Options()
    chrome_options.binary_location = "web-app-ci-cd-with-travis-ci-ZhimaoLin/chromedriver"

    driver = webdriver.Chrome()

    driver.get("http://162.246.157.223:8000")
    elem = driver.find_element_by_id("name")
    assert elem.text == "Zhimao Lin"

    elem = driver.find_element_by_id("about")
    assert elem.text == "I am a computing science student at u of a."

    elem = driver.find_element_by_id("education")
    assert elem.text == "University of Alberta"

    elem = driver.find_element_by_id("skills")
    assert elem.text == "Programming"

    elem = driver.find_element_by_id("work")
    assert elem.text == "Student"

    elem = driver.find_element_by_id("contact")
    assert elem.text == "zhimao@ualberta.ca"
