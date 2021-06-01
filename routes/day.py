from app import app, forbidden
from flask import jsonify, request


@app.route('/day', methods=['POST'])
def day():
    try:
        form = request.form
        _name = form['name']
        _date = form['date']
        if _name and _date and request.method == 'POST':
            message = f"<h1>Hello, {_name}!You were born on {_date}</h1>"
            res = jsonify(message)
            res.status_code = 200
            return res

        else:
            return forbidden()

    except Exception as e:
        print(e)
