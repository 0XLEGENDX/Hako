
from flask import Flask,request
import sqlite3


app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World!"

if(__name__ == "__main__"):
    app.run(debug=False)