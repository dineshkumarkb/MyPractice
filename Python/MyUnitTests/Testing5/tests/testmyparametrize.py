from fixparams import Emp,add_emp
import pytest
import json
import time, random


# Parametrize example 1 without ids
@pytest.mark.parametrize("emp",[Emp("dinesh",1),
                                Emp("user2",2)])
def test_add_emp_1(emp):

    assert emp == add_emp(emp.name, emp.id)


# Parametrize example 2 without ids
@pytest.mark.parametrize("name,id",[("user1",1),
                                    ("user2",2),
                                    ("user3",3)])
def test_add_emp_2(name, id):
    assert Emp(name, id) == add_emp(name, id)


# Parametrize example 3 with ids
test_emps = (Emp("user1",1),
             Emp("user2",2),
             Emp("user3",3),
             Emp("user4",4))

test_id_var = ["Emp({},{})".format(e.name, e.id) for e in test_emps]

@pytest.mark.parametrize('emp',test_emps, ids=test_id_var)
def test_add_emp_3(emp):
    assert emp == add_emp(emp.name, emp.id)


# Parametrize fixtures example 3
def test_emp_fix_1(sample):
    assert sample == add_emp("dinesh",1)

def test_emp_fix_2(myparams):
    assert myparams == add_emp(myparams.name, myparams.id)


def test_built_in_1(test_file_contents):

    # print(f" The file contents are {test_file_contents} ")

    with open(test_file_contents,"r") as f:
        values = json.load(f)

    print(f" The file values are {values} ")

def test_built_in_2(jsonfile):

    with open(jsonfile,"r") as f:
        contents = json.load(f)

    assert "dinesh" == contents.get("name")
    assert 123 == contents.get("empid")


def test_built_in_3(jsonfile):

    with open(jsonfile,"r") as f:
        contents = json.load(f)
    assert "bangalore" == contents.get("loc")


def test_pytest_config(pytestconfig):
    print(f" The myopt value is {pytestconfig.getoption('myopt')} ")
    print(f" The user value is {pytestconfig.getoption('user')} ")


def test_pytest_config_1(user, myopt):
    print(" The user value is ", user)
    print(" The opt value is ", myopt)


# Builtin fixture cache
@pytest.mark.parametrize('i', range(5))
def test_duration(i):
    time.sleep(random.random())

@pytest.mark.parametrize("i", range(5))
def test_session_count():
    print(" Executing test_session_count ")





