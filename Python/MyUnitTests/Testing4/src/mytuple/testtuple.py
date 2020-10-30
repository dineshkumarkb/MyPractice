from collections import namedtuple


MyTask = namedtuple('MyTask',['name','age','id'])


class TaskError(Exception):
    pass


def add_task(name, age, id):
    task = MyTask(name,age,id)
    return task


def check_task_params(name, age, id):
    if isinstance(name,str) and isinstance(age, int) and isinstance(id, int):
        print(" All check passed ")
    raise TaskError(" Invalid params for Task object ")




if __name__ == "__main__":
    print(add_task("dinesh", 32, 123))
    check_task_params("dinesh",32,123)



