# Task
# write a function to fetch data from sql table via api

from flask import Flask, request, jsonify
from API_DB_Task1 import getData,makeConn

app = Flask(__name__)

@app.route('/showinfo',methods=['GET','POST'])
def showData():
    """
    This function only work with post request method and authenticate the user and password credentials,
    and then data from students table of the database gets returned
    :return: json data of the students table
    """
    if (request.method == 'POST'):
        user = request.json['user']
        password = request.json['password']

    # Validating the user and password
    if user == "sunny" and password == "HappyCoding":

        # making connection with the database and getting data from the database
        makeConn()
        data = getData()

        return jsonify(str(data))

if __name__ == '__main__':
    app.run()