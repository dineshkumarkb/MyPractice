class Employee:

    def __init__(self, name):

        self.name = name

    def getName(self):

        return self.name



class TypeSafety:

    def main(self):


        l = []
        l.append(Employee("Dinesh"))
        l.append(Employee("Ganesh"))

        i = iter(l)

        try:
            for ele in i:
                print ele.getName()

        except StopIteration as si:
            print si




t = TypeSafety()
t.main()

