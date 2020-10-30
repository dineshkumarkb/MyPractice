from mytuple import add_task,MyTask,check_task_params, TaskError
import pytest

task_samples = (MyTask("dinesh",21,123),
                MyTask("user2",23,234),
                MyTask("user3",45,3454))

task_ids = ['MyTask({},{},{})'.format(t.name, t.age, t.id) for t in task_samples]

@pytest.mark.parametrize('task',task_samples, ids=task_ids)
def test_add_task(task):
    #result = MyTask(task.name, task.age, task.id)
    assert task == add_task(task.name, task.age, task.id)


@pytest.mark.parametrize('task',[MyTask("dinesh",32,2),
                                  MyTask("kumar",43,3)])
def test_add_task_without_ids(task):
    #result = MyTask(task.name, task.age, task.id)
    assert task == add_task(task.name, task.age, task.id)


@pytest.mark.parametrize("name,age,id",[("dinesh","32",12),
                                        (12,23,34)])
def test_add_exception(name, age, id):
    with pytest.raises(TaskError) as excinfo:
        result = check_task_params(name, age, id)
        print(result)


def test_add_fixture(test_data_1):
    for data in test_data_1:
        assert data == add_task(data.name, data.age, data.id)


def test_file_reader(test_file_contents):
    #print(" the test file contents are ", test_file_contents)
    assert " This is a test " == test_file_contents

# Scope related tests
def test_1(test_session_scope, test_module_scope, test_func_scope):
    print(" Inside scope test ")


class TestScope(object):

    def test_2(self, test_class_scope):
        print(" Inside class scope ")

# End of Scope related tests

def test_file_contents_1(test_file_data_session):
    assert "This is session scope data" == test_file_data_session

@pytest.mark.usefixtures("fileobj")
def test_file_2():
    print(" Testing use fixtures ")


# Parametrize fixture

def test_paramatrize_fixture(test_fix_params):
    print(f" The test fix params are {test_fix_params} ")
    assert MyTask(test_fix_params.name, test_fix_params.age, test_fix_params.id) == test_fix_params


