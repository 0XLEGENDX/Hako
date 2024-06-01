import sqlite3
import json

"""
This class is used to connect to the database.
Database used is sqlite3 in this case and is stored in root folder of the project.
"""
class database:

    def __init__(self) -> None:
        self.sql = sqlite3.connect('database.db')
        self.cur = self.sql.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, phonenumber TEXT, location TEXT, email TEXT, interests TEXT)''')


    def handleInterests(self,interests : list) -> str:
        return json.dumps(interests)

    def insert(self,name : int, age : int, phonenumber :str, location : str , email : str, interests : list)-> None:
        self.cur.execute("INSERT INTO users(name, age, phonenumber, location, email, interests) VALUES(?, ?, ?, ?, ?, ?)", (name, age, phonenumber, location, email, self.handleInterests(interests)))
        self.sql.commit()

    def delete(self,id : int) -> None:
        self.cur.execute("DELETE FROM users WHERE id = ?", (id))
        self.sql.commit()

    def update(self,id: int, name: str, age: int, phonenumber: str, location: str, email: str, interests: list) -> None:
        self.cur.execute("UPDATE users SET name = ?, age = ?, phonenumber = ?, location = ?, email = ?, interests = ? WHERE id = ?", (name, age, phonenumber, location, email, self.handleInterests(interests), id))
        self.sql.commit()

    def getList(self,location : list) -> list:
        self.cur.execute("SELECT * FROM users WHERE location IN " + str(location))
        return self.cur.fetchall()


    def showAllUsers(self)-> list:

        self.cur.execute("SELECT * FROM users")
        return self.cur.fetchall()
    
    def columnNames(self,tableName:str)->list:
        self.cur.execute(f"PRAGMA table_info({tableName})")
        return self.cur.fetchall()
    
    def executeQuery(self,query:str,params:list)->list:
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def exit(self):
        self.sql.close()

