import pymysql
from app import app, forbidden
from db_config import mysql
from flask import jsonify, request

'''
@app.route('/POST_endpoint', methods=['POST'])
def POST_endpoint_function():
    try:
        _form = request.form
        _name = _form['name']
        _password = _form['password']

        if _name and _password and request.method == 'POST':
            # insert record in database
            sqlQuery = "INSERT INTO table_name(name,password) VALUES(%s, %s)"
            data = (_name, _password)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, data)
            conn.commit()
            res = jsonify('Value inserted successfully.')
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()



@app.route('/GET_endpoint', methods=['GET'])
def get_endpoint_function():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("{SELECT QUERY GOES HERE}")
        rows = cursor.fetchall()
        res = jsonify(rows)
        res.status_code = 200
        return res

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()

'''
