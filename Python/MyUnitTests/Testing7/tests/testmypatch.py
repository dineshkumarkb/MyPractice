from monpatch import write_default_cheese,write_cheese,read_cheese,default_pref, TestPatch
import os, monpatch


def test_cheese_pref_home(tmpdir, monkeypatch):
    monkeypatch.setenv("HOME", tmpdir.mkdir('home'))
    write_default_cheese()
    expected = default_pref
    actual = read_cheese()
    assert expected == actual


def test_cheese_pref_fake_home(tmpdir, monkeypatch):
    fake_home = tmpdir.mkdir('home')
    updated_temp_value = "DineshKumar"
    t = TestPatch()
    monkeypatch.setattr(TestPatch,'temp_value', updated_temp_value)
    monkeypatch.setattr(t, 'instance_var', "modifiedsimpleinstance")
    print(" The dynamic inst value is ", t.instance_var)
    print(" The dynamic temp value is ", TestPatch.temp_value)
    monkeypatch.setattr(os.path,'expanduser',lambda x:x.replace('~', str(fake_home)))
    monkeypatch.setitem(default_pref,'pan','thick')
    monkeypatch.setitem(default_pref, 'type', 'veg')
    defaults_mod = default_pref
    write_default_cheese()
    expected = defaults_mod
    actual = read_cheese()
    print(" the actual values are ", actual)
    assert expected == actual