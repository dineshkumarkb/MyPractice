from myfix import make_patch
import myfix


def fake_make_patch():
    return "DineshKumar",32


def make_my_patch():
    name = "Dinesh"
    return name


def test_make_patch(monkeypatch):

    setattr(make_my_patch,"name","DineshKumar")
    monkeypatch.setattr(make_my_patch,"name","DineshKumar")
    #result = make_patch()
    #print(" The result is ", result)