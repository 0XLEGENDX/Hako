
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



@app.route('/getUsers',methods=['POST'])
def getUsers():

    """

    This is the format we accept data in.

    {
    
    "interests": [
    
        "interest1",
        "interest2",
        "interest3"
    ],

    "age":[
        18,25
    ]

    ,

    "location" :[

        "Town",
        "City"
    ]
    
    }

    """
    databaseObj = database.database()

    interests = request.form['interests'].split()
    age = request.form['age'].split()
    location = request.form['location'].split()

    query = "SELECT * FROM users WHERE interests IN (" + ",".join("'" + item + "'" for item in interests) + ") AND age >= " + str(age[0]) + " AND age <= " + str(age[1]) + " AND location IN ( " + "".join("'" + item + "'" for item in location) + ")"
    print(query)
    responce = databaseObj.executeQuery(query,interests + age + location)
    databaseObj.exit()
    return json.dumps(responce)


if(__name__ == "__main__"):
    app.run(debug=True)