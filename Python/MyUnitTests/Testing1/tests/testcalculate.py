import pytest
from src.mycalc.calculate import addme



def testaddme1():
    x = 10
    y = 5
    result = x + y
    print(f" The result is {result} ")
    assert result == addme(x,y)

@pytest.mark.negative
def testaddme2():
    x = -10
    y = 5
    result = x + y
    print(f" The result is {result} ")
    assert result == addme(x, y)



def testaddme3():
    x = 5
    y = 5
    result = 5
    assert result == addme(x, y)


