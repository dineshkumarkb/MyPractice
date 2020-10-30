import pytest
import random, time
from cachetest import greet, myerror


# Builtin fixture cache
@pytest.mark.parametrize("var,", range(5))
def test_count_1(var):
    print("Inside test count")

@pytest.mark.parametrize("var", range(5))
def test_count_2(var):
    time.sleep(random.random())


def test_capsys(capsys):
    greet("Dinesh")
    with capsys.disabled():
        out, err = capsys.readouterr()
        print(" The out value is ", out)
        print(" The error value is ", err)
    assert out == "Hi Dinesh.How are you?\n"
    assert err == ''


def test_capsys_2(capsys):
    myerror("Testing error")
    with capsys.disabled():
        out,err = capsys.readouterr()
        print(" The out is ", out)
        print(" The error is ", err)
    assert "Encountered Testing error" in err






