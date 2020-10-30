from collections import namedtuple

User = namedtuple('User',["name","empid"])

def add_user(name, empid):
    if isinstance(name, str) and isinstance(empid, int):
        print(" Valid params ")
        user = User(name, empid)
        print(" The user value is ", user)
    else:
        raise TypeError("Name and Empid do not match")

    return user



if __name__ == "__main__":
    add_user("dinesh",23)










