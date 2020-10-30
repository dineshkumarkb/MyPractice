import pytest
from fixparams import Emp
import json
import datetime, time


def pytest_addoption(parser):
    parser.addoption("--myopt",action = "store", help = "somerandomoption")
    parser.addoption("--user", action = "store", help = "id the user")

@pytest.fixture(scope="function", name="sample")
def test_data_fix():
    return Emp("dinesh",1)


# Paramterize fixtures

emp_tasks = (Emp("user1",1),
             Emp("user2",2),
             Emp("user3",3),
             Emp("user4",4))

emp_ids = ["Emp({},{})".format(e.name, e.id) for e in emp_tasks]


def get_ids(fix_value):
    t = fix_value
    return "Emp({},{})".format(t.name, t.id)

@pytest.fixture(params=emp_tasks, name="myparams", ids=get_ids)
def test_fix_params(request):
    return request.param


# Built-in Fixtures
@pytest.fixture()
def test_file_contents(tmpdir):

    # Create a json file
    json_dict ={
        "name" : "dinesh",
        "empid": 123
    }

    myjsonfile = tmpdir.join("testjson.json")
    with open(myjsonfile,"w") as f:
        json.dump(json_dict, f)

    return myjsonfile


@pytest.fixture(scope="module", name="jsonfile")
def test_file_module(tmpdir_factory):

    myfile = tmpdir_factory.mktemp("newtmp")
    file_path = myfile.join("emp.json")

    emp_json = {
        "name" : "dinesh",
        "empid" : 123,
        "loc" : "bangalore"
    }

    with open(file_path,"w") as f:
        json.dump(emp_json,f)

    return file_path


@pytest.fixture(name = "user")
def use_pytest_as_fix_1(pytestconfig):
    return pytestconfig.option.user

@pytest.fixture(name = "myopt")
def use_pytest_as_fix_2(pytestconfig):
    return pytestconfig.option.myopt


# Builtin fixture cache
@pytest.fixture()
def check_duration(request, cache):

    key = 'duration/' + request.node.nodeid.replace(":","_")
    start_time = time.time()
    yield
    end_time = time.time()
    current_duration = end_time - start_time
    last_duration = cache.get(key, None)
    cache.set(key, current_duration)
    if last_duration is not None:
        myerror = "Time out"
        assert current_duration <= last_duration * 2, myerror


#
# @pytest.fixture(scope="session")
# def session_count_check(request):
#     key = "datafromprev/sessioncount"
#     prev_count = request.config.cache.get(key,0)
#     yield
#     new_count = prev_count + 1
#     request.config.cache.set(key, new_count)


# @pytest.fixture(autouse=True)
# def check_data_from_prev_new(request, session_count_check):
#     old_cache = session_count_check
#     nodeid = request.node.nodeid
#     yield
#     new_count = old_cache + 1
#     print(" The previous and current session count is {} {} ".format(old_cache, new_count))
#     if old_cache != 0:
#         assert new_count == old_cache + 1



@pytest.fixture(autouse=True)
def check_data_from_prev(request, cache):

    key = "datafromprev/" + request.node.nodeid.replace(":","_")
    yield
    prev_count = cache.get(key, 0)
    curr_count = prev_count + 1
    cache.set(key,curr_count)
    print(" The previous and current session count is {} {} ".format(prev_count, curr_count))
    if prev_count != 0:
        assert curr_count == prev_count + 1










