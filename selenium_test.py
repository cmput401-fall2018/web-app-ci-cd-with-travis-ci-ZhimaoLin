from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def test_home():
    chrome_options = Options()
    chrome_options.binary_location("./chromedriver")

    driver = webdriver.Chrome()

    assert True
