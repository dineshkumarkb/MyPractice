import sqlite3
import os

class DBRowFill(object):

    table_name = "hbinfos"
    key_id = "id"
    key_name = "hb"

    CREATE = " CREATE TABLE IF NOT EXISTS " + table_name + "(" + key_id + " INTEGER PRIMARY KEY AUTOINCREMENT, " + key_name + " TEXT " + ")"

    def __init__(self):
        self.db_name = "hbdict"
        self.conn = sqlite3.connect(DBRowFill.table_name)
        if(self.conn is not None):
            self.create_table()

    def create_table(self):

        try:
            self.conn.execute(DBRowFill.CREATE)

        except Exception as e:
           print e.message


    def insert_data(self,data):
        try:
            self.conn.execute(" INSERT INTO " + DBRowFill.table_name + " (hb) " " VALUES(' " + data + " ') ")

        except Exception as e:
            print e.message


    def get_table(self):
        for row in self.conn.execute(" SELECT * FROM " + DBRowFill.table_name):
            print row



if __name__ == "__main__":
    mydb = DBRowFill()
    for i in xrange(1,10000,1):
        mydb.insert_data(" data " + str(i))
    mydb.get_table()