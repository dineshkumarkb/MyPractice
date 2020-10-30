from ..src import mypatch
#import Testing9


def test1():
    assert 1 == 1


def test2():
    assert 1 == 2


def imported_mod():
    mypatch.method_patch()


def fake_method_patch():

    dynamo_db = "Dinesh"

    return dynamo_db

# class TestPatch(object):
#
#     collection_list = [("name","dinesh"),("age",43)]


def test_patch_method(monkeypatch):

    #setattr(method_patch,"dynamo_db",{"name":"dinesh"})
    monkeypatch.setattr('mypatch.method_patch',fake_method_patch)
    #monkeypatch.setattr(method_patch,"collection_list",[("name","dineshkumar"),("age",43)], raising= False)
    #monkeypatch.setattr(TestPatch, "collection_list", [("name", "dineshkumar"), ("age", 32)], raising=True)
    #expected = getattr(method_patch,"dynamo_db")
    #actual = TestPatch.collection_list
    #print(" The expected result is ", expected)
    #assert expected == actual