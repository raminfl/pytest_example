from unittest import mock

import pytest

from services.main import (add_two_nums_plus_constant, increment_num,
                           silly_get_request)


# @pytest.mark.skip(reason='was tested')
@pytest.mark.parametrize('num, expected_res', [(2, 4), (5, 7)])
@mock.patch('services.main.get_number_one') # mocking get_number_one function
def test_increment_num(mock_get_number_one, num, expected_res):
    mock_get_number_one.return_value = 2
    res = increment_num(num)
    assert res==expected_res

@pytest.mark.parametrize('num1, num2, expected_res',[
        (2,4,10),
        (1,1,6),
        (2,10,16)
        ])
@mock.patch('services.main.CONSTANT', 4) # mocking a variable
def test_add_two_nums_plus_four(num1, num2, expected_res):
    res = add_two_nums_plus_constant(num1, num2)
    assert res==expected_res


@mock.patch('services.main.time.time')
@mock.patch('services.main.random.randint')
@mock.patch('services.main.requests.get')
def test_silly_get_request(mock_get_req, mock_randint, mock_time):
    test_parameters = {
        'timestamp': 123,
        'number': 4
    }
    mock_time.return_value = 123
    mock_randint.return_value = 4
    # for mock_get_req, the return_value itself is a mock object
    mock_requests_return = mock.Mock(**{'status_code':200, 'json.return_value':{'args':test_parameters}})
    mock_get_req.return_value = mock_requests_return
    res = silly_get_request()
    assert res == test_parameters


