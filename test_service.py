from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from service import Service

# def test_bad_random():
#     chrome_options = Options()
#     chrome_options.binary_location = "web-app-ci-cd-with-travis-ci-ZhimaoLin/chromedriver"
#
#     driver = webdriver.Chrome()
#     driver.get("http://162.246.157.223:8000")



def test_bad_random():
    # file = open('/Users/dchui1/datafile', 'r')
    # numberStrings = file.readlines()
    # numbers = [int(x) for x in numberStrings]
    # return random.randint(0, len(numberStrings)-1)
    return

def test_divide():
    return


    # return self.bad_random() / y

def test_abs_plus():
    service = Service()
    assert service.abs_plus(5) == 6
    assert service.abs_plus(-3) == -2





    # return abs(x) + 1

def test_complicated_function(x):
    # return divide(x), bad_random % 2
    return


    # elem = driver.find_element_by_id("name")
    # assert elem.text == "Zhimao Lin"
    #
    # elem = driver.find_element_by_id("about")
    # assert elem.text == "I am a computing science student at u of a."
    #
    # elem = driver.find_element_by_id("education")
    # assert elem.text == "University of Alberta"
    #
    # elem = driver.find_element_by_id("skills")
    # assert elem.text == "Programming"
    #
    # elem = driver.find_element_by_id("work")
    # assert elem.text == "Student"
    #
    # elem = driver.find_element_by_id("contact")
    # assert elem.text == "zhimao@ualberta.ca"

