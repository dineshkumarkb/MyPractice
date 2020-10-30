import pytest

pytest_plugins = 'pytester'


@pytest.fixture()
def test_sample(testdir):
    testdir.makepyfile("""
    
         def test1():
            assert 0 == 0
            
         def test2():
            assert 1 == 2
    
    """)

    return testdir