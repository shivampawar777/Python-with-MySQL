import mysql.connector as connector

class Student:
    def __init__(self):
        self.con = connector.connect(host="localhost", user="root", password="root", database="Test", port="3306")
        print("Connected to Database...")

        query = 'create table if not exists Students(SID int primary key, Name varchar[200], City varchar[100])'
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Table Students created...")

    def insert(self, id, name, city):
        query = "insert into Students(SID={}, Name='{}', City='{}')".format(id, name, city)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print(id, name, city)

    def update(self,id, name, city):
        query = "update user set Name='{}', City='{}' where SID={}".format(name, city, id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        print("Data upadated...")

    def delete(self, id):
        query = "delete from Students where SID = {}".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        print("Data deleted...")

    def fetch_all(self):
        query = 'select * from Students'
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()

        for row in cur:
            print(row)

        print("***...Data...***")
