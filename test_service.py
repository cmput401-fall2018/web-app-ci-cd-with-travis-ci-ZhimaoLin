from mock import patch
from service import Service


@patch('service.Service.bad_random')
def test_bad_random(bad_random):
    service = Service()
    bad_random.return_value = 10
    assert service.bad_random() == 10


@patch('service.Service.bad_random')
def test_divide(bad_random):
    service = Service()

    # Test 0 / x, such that x > 0
    bad_random.return_value = 0
    assert service.divide(5) == 0

    # Test 0 / x, such that x < 0
    bad_random.return_value = 0
    assert service.divide(-5) == 0

    # Test y / x such that y > 0 and x > 0
    bad_random.return_value = 6
    assert service.divide(3) == 2

    # Test y / x such that y > 0 and x < 0
    bad_random.return_value = 6
    assert service.divide(-3) == -2

    # Test y / x such that x = 0
    bad_random.return_value = 6
    try:
        service.divide(0)
    except ZeroDivisionError:
        assert True


def test_abs_plus():
    service = Service()

    # Test x > 0
    assert service.abs_plus(5) == 6

    # Test x = 0
    assert service.abs_plus(0) == 1

    # Test x < 0
    assert service.abs_plus(-3) == 4


@patch('service.Service.bad_random')
@patch('service.Service.divide')
def test_complicated_function(divide, bad_random):
    service = Service()

    # divide > 0 and bad_random = 0
    divide.return_value = 5
    bad_random.return_value = 0
    result = service.complicated_function(6)
    assert result[0] == 5
    assert result[1] == 0

    # divide = 0 and bad_random = 0
    divide.return_value = 0
    bad_random.return_value = 0
    result = service.complicated_function(6)
    assert result[0] == 0
    assert result[1] == 0

    # divide < 0 and bad_random = 0
    divide.return_value = -6
    bad_random.return_value = 0
    result = service.complicated_function(6)
    assert result[0] == -6
    assert result[1] == 0

    # divide < 0 and bad_random > 0
    divide.return_value = -6
    bad_random.return_value = 7
    result = service.complicated_function(6)
    assert result[0] == -6
    assert result[1] == 7 % 2

    # divide = 0 and bad_random > 0
    divide.return_value = 0
    bad_random.return_value = 7
    result = service.complicated_function(6)
    assert result[0] == 0
    assert result[1] == 7 % 2

    # divide > 0 and bad_random > 0
    divide.return_value = 6
    bad_random.return_value = 7
    result = service.complicated_function(6)
    assert result[0] == 6
    assert result[1] == 7 % 2
