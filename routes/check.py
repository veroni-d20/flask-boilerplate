import pymysql
from app import app, forbidden
from db_config import mysql
from flask import jsonify, request


@app.route('/check', methods=['GET'])
def check():
    try:
        _form = request.form
        _name = _form['name']
        if _name and request.method == 'GET':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            try:
                query = f"SELECT name FROM details WHERE name='{_name}'"
                # print(query)
                cursor.execute(query)
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                res = jsonify(rows)
                row = rows[0]
                res.status_code = 200
                if _name == row["name"]:
                    print(f"{_name} == {row}")
                    return "True"
                # else:
                #     # print(f"{_name} != {row}")
                #     return "False"
            except Exception as e:
                msg = "Not found in the database"
                mess = jsonify(msg)
                return mess
        else:
            return forbidden()

    except Exception as e:
        print(e)
'''
    finally:
        cursor.close()
        conn.close()
        '''