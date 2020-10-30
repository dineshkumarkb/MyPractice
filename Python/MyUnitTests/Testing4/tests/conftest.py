import pytest
from mytuple import MyTask
import os, time, datetime


@pytest.fixture()
def test_data_1():
    return (MyTask("user1",23,123),
            MyTask("user2","32",234),
            MyTask("user3",43,456))


@pytest.fixture()
def test_file_contents(tmpdir):
    file_name = os.path.join(str(tmpdir), "file1.txt")
    print(" The file name is ", file_name)
    with open(file_name,"w+") as f:
        f.write(" This is a test ")
        f.seek(0)
        content = f.read()
        print(" The content is ", content)
    return content

# All scope related fixtures tests start

@pytest.fixture(scope="function")
def test_func_scope():
    return "Function scope"


@pytest.fixture(scope="module")
def test_module_scope():
    return "Module scope"


@pytest.fixture(scope="session")
def test_session_scope():
    return "Session scope"


@pytest.fixture(scope="class")
def test_class_scope():
    return "Class scope"


# All scope related features test end


@pytest.fixture(scope="session")
def test_file_data_session(tmpdir_factory):
    temp_path = tmpdir_factory.mktemp("temp")
    file_path = os.path.join(str(temp_path),"file2.txt")
    print(" The file path is ", file_path)
    with open(file_path,"w+") as f:
        f.write("This is session scope data")
        f.seek(0)
        contents = f.read()
        return contents


@pytest.fixture(scope="session", name="fileobj")
def create_file_fixture(tmpdir_factory):
    temp_path = tmpdir_factory.mktemp("tempfolder")
    file_path = os.path.join(str(temp_path),"file1.txt")
    with open(file_path,"w+") as f:
        f.write("Test content inside file")


@pytest.fixture(scope="session", autouse=True)
def test_timers():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f" The execution time is {end_time - start_time}")


# Fixtures parametrization

task_examples = (MyTask("dinesh",32,123),
                 MyTask("user1",43,1234))




def get_my_ids(fixture_value):
    t= fixture_value
    mytask_ids = 'MyTask({},{},{})'.format(t.name, t.age, t.id)
    return mytask_ids



@pytest.fixture(params=task_examples, ids= get_my_ids)
def test_fix_params(request):
    print(f" The param is {request.param} ")
    return request.param










