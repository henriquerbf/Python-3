from flask import Flask, jsonify, request

import pyodbc 
connectionString = pyodbc.connect('DRIVER={Devart ODBC Driver for SQL Server};Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;')

app = Flask(__name__)

numbers = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
]

@app.route('/getValueIndex/<int:numberReceived>', methods=['GET'])
def getValueIndex(numberReceived):
    return jsonify(numbers.index(numberReceived))
        
app.run(port=8080, host='localhost', debug=True);