from collections import namedtuple
import json

Employee = namedtuple("Employee", field_names=["name", "id", "date", "status"])

emp = Employee("admin", "1", "Oct 22 2020", "employed")

updated_emp = emp._replace(id=2)
print(updated_emp)

emp = Employee._make(["user1", "3", "Oct 22 2020", "employed"])
print(emp)