from myexcept import User,add_user
import pytest


def test_add_user_excpt():
    name = 123
    empid = 123
    with pytest.raises(TypeError) as excinfo:
        result = add_user(name, empid)
        print(f" The result is {result} ")
    print(f" The exc info is {excinfo.value.args} ")


@pytest.mark.xfail
def test_add_user_no_excpt():
    name = "dinesh"
    empid = 123
    with pytest.raises(TypeError) as excinfo:
        result = add_user(name, empid)
        print(f" The result is {result} ")
    print(f" The exc info is {excinfo.value.args} ")
