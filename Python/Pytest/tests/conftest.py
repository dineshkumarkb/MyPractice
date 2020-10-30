import pytest
from mytasks import calc
from .test_calc import connect_me

@pytest.fixture
def start_sqlite(tmpdir):
    connect_me(str(tmpdir),"dinesh_db")


@pytest.fixture(scope="function")
def swap_me():
    return (1,2)

@pytest.fixture(name="dinesh")
def just_return():
    return (25,35)


