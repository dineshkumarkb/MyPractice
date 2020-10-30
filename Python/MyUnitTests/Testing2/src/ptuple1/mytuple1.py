from collections import namedtuple

Task = namedtuple("Task",["name","id"])


def add_task(name,id):
    task = Task(name,id)
    return task



