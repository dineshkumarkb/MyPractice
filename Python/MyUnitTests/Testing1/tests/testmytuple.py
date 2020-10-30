from collections import namedtuple
from src.mynamedtuple.mytuple import tupme1, Task


def testtupme1():
    task = Task("Dinesh",32,"Madurai")
    assert task == tupme1()