import sqlite3

db = sqlite3.connect("tutorial.db")

name = input("what is your name?")
print("Hello",name)