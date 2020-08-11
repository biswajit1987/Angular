import flask
import mysql.connector as mysql
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

HOST = ''
DATABASE = ''
USER = "demo"
PASSWORD = "Password@1"


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome</h1>
<p>API.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/users/all', methods=['GET'])
def api_all():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    mycursor = db_connection.cursor()
    mycursor.execute("SELECT * FROM demousers")
    myresult = mycursor.fetchall()
    return jsonify(myresult)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/users', methods=['GET'])
def api_filter():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    query_parameters = request.args

    ids = query_parameters.get('id')
    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')

    query = "SELECT * FROM demousers WHERE"
    to_filter = []

    if ids:
        query += ' id=%s AND'
        to_filter.append(ids)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if email:
        query += ' email=%s AND'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s AND'
        to_filter.append(mobile)

    if not (ids or mobile or email or name):
        return page_not_found(404)

    query = query[:-4]
    cursor.execute(query, to_filter)
    results = cursor.fetchall()

    return jsonify(results)


@app.route('/users', methods=['POST'])
def update_users():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    cursor = db_connection.cursor()
    query_parameters = request.args

    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')
    password = query_parameters.get('password')
    introduction = query_parameters.get('introduction')

    query = 'INSERT INTO demousers (name, mobile, password, introduction, email) VALUES (%s, %s, %s, %s, %s)'
    to_filter = (name, mobile, password, introduction, email)

    if not (introduction or mobile or email or name or password):
        return page_not_found(404)

    cursor.execute(query, to_filter)
    #results = cursor.fetchall()
    db_connection.commit()
    return "Record inserted."


@app.route('/users', methods=['DELETE'])
def delete_users():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    query_parameters = request.args

    ids = query_parameters.get('id')
    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')

    query = "DELETE FROM demousers WHERE"
    to_filter = []

    if ids:
        query += ' id=%s AND'
        to_filter.append(ids)
    if name:
        query += ' name=%s AND'
        to_filter.append(name)
    if email:
        query += ' email=%s AND'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s AND'
        to_filter.append(mobile)

    if not (ids or mobile or email or name):
        return page_not_found(404)

    query = query[:-4]
    cursor.execute(query, to_filter)
    db_connection.commit()

    return "Record delete."


@app.route('/users', methods=['PUT'])
def update():
    db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD)
    db_connection.row_factory = dict_factory
    cursor = db_connection.cursor()
    query_parameters = request.args

    introduction = query_parameters.get('introduction')
    name = query_parameters.get('name')
    email = query_parameters.get('email')
    mobile = query_parameters.get('mobile')
    password = query_parameters.get('password')
    ids = query_parameters.get('id')

    query = "UPDATE demousers SET"
    to_filter = []

    if introduction:
        query += ' introduction=%s ,'
        to_filter.append(introduction)
    if name:
        query += ' name=%s ,'
        to_filter.append(name)
    if email:
        query += ' email=%s ,'
        to_filter.append(email)
    if mobile:
        query += ' mobile=%s ,'
        to_filter.append(mobile)
    if password:
        query += ' password=%s'
        to_filter.append(password)
    if ids:
        query += ' WHERE id=%s'
        to_filter.append(ids)

    if not (introduction or mobile or email or name or ids):
        return page_not_found(404)

    cursor.execute(query, to_filter)
    db_connection.commit()

    return "Record update."


app.run()
