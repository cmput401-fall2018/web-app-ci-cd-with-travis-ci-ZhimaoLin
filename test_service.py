from mock import patch
import io
from service import Service


@patch('io.open')
@patch('io.FileIO.readlines')
def test_bad_random():
    io.open.return_value = 0
    io.FileIO.readlines.return_value = '123456'

    service = Service()
    result = service.bad_random()

    assert result >= 0
    assert result < 5

    # file = open('/Users/dchui1/datafile', 'r')
    # numberStrings = file.readlines()
    # numbers = [int(x) for x in numberStrings]
    # return random.randint(0, len(numberStrings)-1)
    return


@patch('service.Service.bad_random')
def test_divide(bad_random):
    service = Service()

    bad_random.return_value = 0
    assert service.divide(5) == 0

    bad_random.return_value = 6
    assert service.divide(3) == 2


def test_abs_plus():
    service = Service()
    assert service.abs_plus(5) == 6
    assert service.abs_plus(-3) == 4


@patch('service.Service.bad_random')
@patch('service.Service.divide')
def test_complicated_function(divide, bad_random):
    service = Service()

    divide.return_value = 0
    bad_random.return_value = 0
    result = service.complicated_function(6)
    assert result[0] == 0
    assert result[1] == 0

    divide.return_value = 6
    bad_random.return_value = 7
    result = service.complicated_function(6)
    assert result[0] == 6
    assert result[1] == 7 % 2
