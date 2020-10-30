from collections import namedtuple


Emp = namedtuple('Emp',["name","id"])


def add_emp(name, id):
    return Emp(name,id)



if __name__ == "__main__":
    print(add_emp("dinesh",123))
