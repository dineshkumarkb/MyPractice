from collections import namedtuple


Task = namedtuple("Task",["name","age","location"])


def tupme1():

    task = Task("Dinesh",32,"Madurai")
    print(f" The task is {task} ")
    return task

