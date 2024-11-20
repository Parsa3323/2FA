from flask import Flask, render_template, jsonify, request, g, redirect, make_response
import sqlite3
import DataBaseManager
import json
import Main
import random

DATABASE = 'data.db'

app = Flask(__name__, template_folder='public')
def get_db():
    """Open a new database connection if not already established"""
    if 'db_conn' not in g:
        # Open the database connection with check_same_thread=False
        g.db_conn = sqlite3.connect(DATABASE, check_same_thread=False)
        g.db_conn.row_factory = sqlite3.Row  # Enable column access by name
    return g.db_conn

# Function to close the database connection
@app.teardown_appcontext
def close_db(error):
    """Close the database connection after the request is finished"""
    db_conn = getattr(g, 'db_conn', None)
    if db_conn is not None:
        db_conn.close()
@app.route('/')
def yo():
    return True
@app.route('/Main', methods=['POST', 'GET'])
def main():
    thin = "sd"
    yo = request.args.get('username')
    if request.method == 'POST':
        thin = request.form.get('Pin')
        print(thin)
    return render_template(template_name_or_list='index.html', yo=yo)
@app.route('/go', methods=['POST'])
def POsST():
    code = request.form.get('Pin')
    valr = Main.get_and_check(user="None", code_provided=code)
    if request.args.get('username') is not None:
        username = request.args.get('username')
        conns = get_db()  # Fetch the connection from g
        table_name = "users"
        keys = DataBaseManager.get_from_table(conns, 'users')
        print('yoo::')
        print(keys)
        # json_keys = json.load(keys)
        keyss = next((item['key'] for item in keys if item['name'] == username), None)

        ohh = Main.check_from_custom_key(key=keyss, code_provided=code)
        if ohh is True:
            return "yoooo"
        else:
            return 'ass'
    if valr is not False:
        return "yoo sighned up succses"
    else:
        return "sorry"
    # thin = "sd"
    # if request.method == 'POST':
    #     thin = request.form.get('Pin')
    #     print(thin)
    # return thin
@app.route('/create-accc')
def create():
    return render_template('CreateAcc.html')



@app.route('/to', methods=['POST'])
def to():
    username = request.form.get('username')
    password = request.form.get('pass')
    key = Main.create_a_key()
    print(key)
    user_data = {"name": username, "key": key}

    # Get a database connection and insert data into the table
    conn = get_db()  # Fetch the connection from g
    table_name = "users"
    DataBaseManager.insert_into_table(conn, table_name, user_data)

    datas = {
        'name': username,
        'key': key
    }
    return jsonify(datas)

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/check-login', methods=['POST'])
def check_login():
    username = request.form.get('username')
    return redirect(f'/Main?username={username}')


if __name__ == '__main__':
    with app.app_context():
        conn = get_db()  # Now within app context, so it's safe to get the DB
        table_name = "users"
        columns = {"name": "TEXT", "key": "TEXT"}
        DataBaseManager.create_table(conn, table_name, columns)

    app.run(debug=True)
