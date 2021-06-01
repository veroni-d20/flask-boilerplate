import pymysql
from app import app, forbidden
from db_config import mysql
from flask import jsonify, request


@app.route('/display', methods=['GET'])
def display():
    try:
        _form = request.form
        _password = _form['password']
        if _password and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = f"SELECT name FROM cortex.details WHERE password='{_password}'"
            # print(query)
            cursor.execute(query)
            rows = cursor.fetchall()
            # cursor.close()
            # conn.close()
            res = jsonify(rows)
            res.status_code = 200
            return res
        else:
            return forbidden()

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        conn.close()
