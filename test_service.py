from mock import patch
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

@patch('bad_random')
def test_divide(bad_random):
    bad_random.return_value = 0

    service = Service()
    assert service.divide(5) == 0


    # return self.bad_random() / y

def test_abs_plus():
    service = Service()
    assert service.abs_plus(5) == 6
    assert service.abs_plus(-3) == 4





    # return abs(x) + 1

def test_complicated_function():
    # return divide(x), bad_random % 2
    return

