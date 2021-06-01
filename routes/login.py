from app import app, forbidden
from db_config import mysql
from flask import jsonify, request


@app.route('/login', methods=['POST'])
def login():
    try:
        _form = request.form
        _name = _form['name']
        _password = _form['password']

        if _name and _password and request.method == 'POST':
            # insert record in database
            sqlQuery = "INSERT INTO details(name,password) VALUES(%s, %s)"
            data = (_name, _password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, data)
            conn.commit()
            message = f"<h1>Hello, {_name}!You have successfully logged in!!</h1>"
            res = jsonify(message)
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
