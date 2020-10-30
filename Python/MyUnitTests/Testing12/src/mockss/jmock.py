import json


def load_data():
    data = '{"name":"dinesh"}'
    jsonified_data = json.loads(data)
    print(f" The data is {jsonified_data} ")
    name = jsonified_data.get('name')
    age = another_func()
    print(f" The name is {name} ")
    print(f" The age is {age}")
    return age





def another_func():
    return {"age":22}