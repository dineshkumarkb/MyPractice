class EmpStats(object):

    def __init__(self, name, id):
        self.user_name = name
        self.user_id = id

    @property
    def name(self):
        return self.user_name

    @name.setter
    def name(self, new_name):
        self.user_name = new_name

    def __str__(self):
        return f"EmpStats({self.id})"



c = EmpStats("Dinesh",123)
print(c.name)