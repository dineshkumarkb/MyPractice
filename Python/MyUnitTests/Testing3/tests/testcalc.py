from myexcept import addnum,subnum,divnum,mulnum
import pytest

# Tests to demonstrate mark, skip, skipif, x fail

def test_addnum():
    x = 10
    y = 5
    result = x + y
    assert result == addnum(x,y)


@pytest.mark.xfail
def test_fail_addnum():
    x = -5
    y = -5
    result = x - y
    assert result ==  addnum(x, y)


@pytest.mark.xfail
def test_fail_addnum_1():
    x = -5
    y = -5
    result = x + y
    assert result ==  addnum(x, y)


@pytest.mark.duplicate(reason = "This is a duplicate no 1")
def test_addnum_dup1():
    x = 10
    y = 5
    result = x + y
    assert result == addnum(x,y)

@pytest.mark.duplicate(reason = "This is a duplicate no 2")
def test_addnum_dup2():
    x = 10
    y = 5
    result = x + y
    assert result == addnum(x, y)



