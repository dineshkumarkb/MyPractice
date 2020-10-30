from mockss import load_data
from mockss.jmock import load_data
from unittest.mock import patch
import pytest
from mockss.jmock import another_func


@patch('mockss.jmock.load_data')
@patch('mockss.jmock.another_func')
@patch('json.loads')
def test_load_data(mock_json, mock_age, mock_var):

    mock_json.return_value = {"name":"dineshkumar"}
    print(f" The name is {mock_json()}")
    mock_age.return_value = {'age': 25}
    mock_var.age.return_value = mock_age()
    print(f" The mock variable is {mock_var.age()}")
    response = load_data()
    print(f" The response is {response} ")
    #assert response == mock_json().get('name')
    print(" Mock age is ", mock_age())
    assert response == mock_var.age()


