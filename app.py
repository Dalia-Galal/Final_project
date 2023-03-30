import sqlite3

db = sqlite3.connect("tutorial.db")
cur = db.cursor()
db.execute("create table habits (name , yes , no)")
name = input("what is your name?")
print("Hello",name)