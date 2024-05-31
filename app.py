
from flask import Flask,request, render_template
import sqlite3
import json
from modules import database


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

@app.route('/showDatabase')
def showDatabase():
    databaseObj = database.database()
    requestResult = databaseObj.showAllUsers()
    columnsRequest = databaseObj.columnNames("users")
    databaseObj.exit()
    return render_template('showDatabase.html',query="Select * From users;",databaseName="users",columns = [column[1] for column in columnsRequest],requestResult=requestResult)

if(__name__ == "__main__"):
    app.run(debug=False)