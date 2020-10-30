from ptuple1 import add_task, Task

def test_add_task():
    task = Task("Dinesh",123)
    assert task == add_task("Dinesh",123)