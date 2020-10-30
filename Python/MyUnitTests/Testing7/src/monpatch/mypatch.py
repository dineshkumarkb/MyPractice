import os
import json

default_pref = {
    'pan' : ['thin','thick'],
    'type' : ['veg', 'nonveg'],
    'extra' : ['tomato', 'jalapenos']
}

class TestPatch(object):
    temp_value = "Dinesh"

    def __init__(self):
        self.instance_var = "simpleinstance"

def read_cheese():
    path = '~/cheese.json'
    full_path = os.path.expanduser(path)
    print(" The full path is ", full_path)
    with open(full_path,'r') as f:
        contents = json.load(f)

    return contents


def write_cheese(pref):
    path = '~/cheese.json'
    full_path = os.path.expanduser(path)
    print(" The full path is ", full_path)
    with open(full_path,'w') as f:
         json.dump(pref,f, indent=4)


def write_default_cheese():
    path = '~/cheese.json'
    full_path = os.path.expanduser(path)
    print(" The full path is ", full_path)
    with open(full_path,'w') as f:
         json.dump(default_pref,f, indent=4)