import sqlite3



def method_patch():

    collection_list = []

    dynamo_db = {"name":"dinesh","age":32}

    for items in dynamo_db.items():
        collection_list.append(items)

    return collection_list