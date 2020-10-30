from cachetest import mycalculatormod
import pytest


@pytest.fixture(autouse=True)
def add_mc(doctest_namespace):
    doctest_namespace["mc"] = mycalculatormod