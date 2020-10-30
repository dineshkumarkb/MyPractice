import importlib


mymodule = importlib.import_module("MyReflect")
myclass = getattr(mymodule,"Person")
print(myclass().name)
myclass().age