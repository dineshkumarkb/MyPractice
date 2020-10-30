from collections import namedtuple
from mymock.mockme1 import call_me


Emp = namedtuple('Emp',["name","age"])


def add_emp(name, age):
    return Emp(name, age)


def add(x, y):

    if not (isinstance(x, int) and isinstance(y, int)):
        raise TypeError
    return x + y


def func_call():
    call_result = call_me()
    return call_result