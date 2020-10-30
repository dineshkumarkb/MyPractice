import pytest
from mytasks import calc
import sqlite3,os


def test_add():
    op = calc.add(1,2)
    assert (1+2) == op


def connect_me(path, name):
    absolute_path = os.path.join(path,name)
    conn = sqlite3.connect(absolute_path)
    print(" The db conn result is ", conn)

def test_swap(start_sqlite):
    op = calc.add(1,4)
    assert (4+1) == op

@pytest.mark.negvalues
def test_add_minus():
    op = calc.add(-1,2)
    assert (-1+2) == op

@pytest.mark.negvalues
def test_add_minus_all():
    op = calc.add(-3,-4)
    assert ((-3)+(-4)) == op

def test_sub():
    assert (1-2) == calc.sub(1,2)


testdata = [(1,2,3),(3,4,7),(7,3,10),(-1,-4,-5)]

@pytest.mark.parametrize("num1,num2,expected",testdata)
def test_add_params(num1,num2,expected):
    op = calc.add(num1,num2)
    assert op == expected



@pytest.mark.parametrize('num1,num2,expected',testdata,ids=["input1","input2","input3","input_negative"])
def test_add_params_2(num1,num2,expected):
    op = calc.add(num1,num2)
    assert op == expected



def test_swap_number(swap_me):
    op = calc.add(1,2)
    assert swap_me[0] + swap_me[1] == op


def test_return_fix(dinesh):
    print(" The value is {} ".format(dinesh))
    for n in dinesh:
        print(n)
    assert 25 in dinesh


test_data_3 = [{"collectionId":"123","copystatus":"completed"},{"collectionId":"456","copystatus":"failed"}]


@pytest.mark.parametrize("metadata",test_data_3)
def test_copy_status(metadata):
    print(" Calling the method ")
    assert True == calc.validate_ids(metadata)
    print(" Call complete")


# Test tmp_dir fixture
def test_tmp_dir_fix(tmpdir):

    a_file = tmpdir.join("something.txt")
    a_sub_dir = tmpdir.mkdir("anything")

    another_file = a_sub_dir.join("something_else.txt")
    a_file.write(" These are the contents of a_file ")

    another_file.write(" These are the contents of another file ")

    assert  a_file.read() == " These are the contents of a_file "
    assert  another_file.read() == " These are the contents of another file "


# Test tmpdir factory fixture
def test_tmpdir_factory_fix(tmpdir_factory):

    a_dir = tmpdir_factory.mktemp("mydir")

    base_temp = tmpdir_factory.getbasetemp()
    print(" The base dir is ", base_temp)

    a_file = a_dir.join("something.txt")
    a_file.write(" These are the contents of a_file ")

    a_sub_dir = a_dir.mkdir("anything")
    another_file = a_sub_dir.join("something_else.txt")
    another_file.write(" These are the contents of another file ")

    assert a_file.read() == " These are the contents of a_file "
    assert another_file.read() == " These are the contents of another file "








