import sqlite3
import json

sql = sqlite3.connect('database.db')
cur = sql.cursor()


cur.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phonenumber TEXT, location TEXT, email TEXT, interests TEXT)''')


def handleInterests(interests : list) -> str:
    return json.dumps(interests)

def insert(name : int, age : int, phonenumber :str, location : str , email : str, interests : list)-> None:
    cur.execute("INSERT INTO users(name, age, phonenumber, location, email, interests) VALUES(?, ?, ?, ?, ?, ?)", (name, age, phonenumber, location, email, handleInterests(interests)))
    sql.commit()

def delete(id):
    cur.execute("DELETE FROM users WHERE id = ?", (id))
    sql.commit()

def update(id, name, age, phonenumber, location, email, interests):
    cur.execute("UPDATE users SET name = ?, age = ?, phonenumber = ?, location = ?, email = ?, interests = ? WHERE id = ?", (name, age, phonenumber, location, email, handleInterests(interests), id))
    sql.commit()

def getList(location : list) -> list:
    cur.execute("SELECT * FROM users WHERE location IN " + str(location))
    return cur.fetchall()



