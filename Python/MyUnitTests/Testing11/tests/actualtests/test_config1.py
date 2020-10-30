import pytest
from unittest.mock import Mock,patch
from mymock import Emp,add_emp,add, call_me, function_1
import mymock


# def test1():
#     print(" Inside test 1 ")
#     num1 = 1
#     num2 = 1
#     assert num1 == num2
#
#
# @pytest.mark.xfail
# def test2():
#     assert 2 == 2
#
# @pytest.mark.smoke
# def test_marker_1():
#     assert 2 == 2
#
# def check_me():
#     print(" Inside check me ")
#     assert "check" == "check"

myemp = add_emp("dinesh",23)

def test_add_emp():
    #mocker.patch("mymock.mockme")
    # m = mocker.patch.object(mymock,'add_emp', return_value=myemp)
    # #print(m)
    # add_emp("dinesh",23)
    # mymock.add_emp.assert_called_once_with("dinesh",23)
    #actual = add_emp("dinesh",23)
    #assert actual == myemp
    mock = Mock()
    # Mock's ability to declare/define methods on the fly
    mock.call_me("name","age")
    mock.call_me("fullname","id")
    print(" The mock object is ", mock)
    print(mock.call_me.call_count)
    print(mock.call_me.call_args)
    print(mock.call_me.call_args_list)
    print(mock.method_calls)
    mock.add_emp.return_value = myemp
    assert add_emp("dinesh",23) == myemp
    #mock.call_me.assert_called()
    #mock.call_me.assert_called_once()
    #mock.call_me.assert_called_with("name","age")
    #mock.call_me.assert_called_once_with("name","age")


addition = add(1,2)
#add_err = add("3","2")

def test_add_num():
    mock = Mock(side_effect=TypeError)
    mock.add.return_value = addition
    #mock.add.side_effect = TypeError
    #with mock.assertRaises(TypeError):
    with pytest.raises(TypeError):
        add("3","2")


def test_add_num_1():
    mock = Mock()
    mock.add.return_value = addition
    result = mock.add()
    assert result == addition


@patch('mymock.mockme')
def test_add_patch(mock_add):
    mock_add.add_emp.return_value = myemp
    result = mock_add.add_emp()
    assert result == myemp


@patch('mymock.mockme')
def test_add_patch_typeerror(mock_add):
    mock_add.add_emp.side_effect = TypeError
    with pytest.raises(TypeError):
        mock_add.add_emp()


def test_add_patch_context():
    with patch("mymock.mockme") as mock_add:
        mock_add.add_emp.side_effect = TypeError
        with pytest.raises(TypeError):
            mock_add.add_emp()


@patch.object(mymock.mockme,'add_emp',return_value = myemp)
def test_add_patch_object(myobject):
    result = myobject()
    assert result == myemp

@patch("mymock.mockme1")
@patch("mymock.mockme")
def test_func_call(mock_call, mock_call_1):
    mock_call_1.call_me.return_value = "Callme"
    mock_call.func_call.call_result.return_value = mock_call_1.call_me()
    mock_call.func_call.return_value = mock_call.func_call.call_result()
    print(mock_call.func_call())

@patch("mymock.mockme1.function_1")
def test_function_1(mock_test_value):
    mock_test_value.test_value.return_value = 'mocked_value'
    print("The mocked test value is ", mock_test_value.test_value())
    mock_test_value.return_value = 'mocked_value'
    assert mymock.mockme1.function_1.test_value() == 'mocked_value'
    assert mymock.mockme1.function_1() == mock_test_value()










if __name__ == "__main__":
    test_add_emp()
