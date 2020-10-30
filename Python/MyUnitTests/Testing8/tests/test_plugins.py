from pytest_nice import Emp, add_emp
import pytest


def test_failures():
    name = "dinesh"
    age = 123
    with pytest.raises(TypeError):
        add_emp(name, age)
