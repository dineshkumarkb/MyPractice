from collections import namedtuple

Emp = namedtuple("Emp",["name","age"])


def add_emp(name, age):
    if isinstance(name, str) and isinstance(age, int):
        print(" The instance types are right ")
        return Emp(name,age)
    else:
        print(" Raising Type Error ")
        raise TypeError
