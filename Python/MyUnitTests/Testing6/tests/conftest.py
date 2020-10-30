import pytest
from collections import namedtuple
from datetime import datetime
from cachetest import mycalculatormod


@pytest.fixture()
def add_mc(doctest_namespace):
    doctest_namespace["mc"] = mycalculatormod


# Builtin fixture cache
@pytest.fixture()
def check_count(request, cache):

    key = 'testcount/' + request.node.nodeid.replace(":","_")
    yield
    prev_count = cache.get(key,0)
    current_count = prev_count + 1
    cache.set(key,current_count)
    if prev_count is not None:
        assert current_count == prev_count +1
    print(" The current count and previous count are ",current_count,prev_count)

Duration = namedtuple('Duration',['current', 'last'])

# Cache entry change
@pytest.fixture(scope="session")
def duration_cache(request):
    key =  "duration/testduration"
    d = Duration({},request.config.cache.get(key,{}))
    yield d
    request.config.cache.set(key,d.current)


@pytest.fixture()
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    print(" The nodeid is ", nodeid)
    start_time = datetime.now()
    yield
    time_diff = (datetime.now() - start_time).total_seconds()
    d.current[nodeid] = time_diff
    if d.last.get(nodeid,None) is not None:
        assert time_diff <= (d.last[nodeid] * 2) , "Error in time"


@pytest.fixture(scope="session")
def calc_count(request):
    key = "test/count"
    sess_count = request.config.cache.get(key,0)
    print(" Session started ")
    yield sess_count
    print(" Session ended ")
    current_count = sess_count + 1
    request.config.cache.set(key, current_count)


@pytest.fixture(autouse=True)
def check_my_count(request, calc_count):
    mycount = calc_count
    nodeid = request.node.nodeid
    yield

    print(" The mycount value is ", mycount)
    print(" The nodeid is ", nodeid)






