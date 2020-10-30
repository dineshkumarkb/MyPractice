# n = [1,34,55,4,8]
#
# x = n[-3::-1]
#
# print(x)
#
# #Output : [55,34,1]



# while(True):
#     choice = (input("Are you signed up? (y/n) "))
#
#     if choice == "y" or choice == "n":
#         print(f"Your choice is {choice}")
#         break


class PropTest(object):

    def __init__(self):
        self._name = "Dinesh"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value





p = PropTest()
#p._name = "new name"
p.name = "Kumar"
print(p.name)