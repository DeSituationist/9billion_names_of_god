from flask import Flask, render_template, request, redirect, url_for, session
from waitress import serve
from typing import *
import logging
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_DB = os.path.join(BASE_DIR, 'orders.db')
ACCOUNTS_DB = os.path.join(BASE_DIR, 'accounts.db')

logging.basicConfig(level=logging.INFO)

#DataBases
con = sqlite3.connect(ORDERS_DB)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS orders(name, drink, flavor, topping);')
con = sqlite3.connect(ACCOUNTS_DB)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS accounts(nickname, email, password, rank);')

#Flask app
app = Flask(__name__)
app.secret_key = 'any-random-string'

@app.route('/order', methods = ['GET'])
def show_order():
    drinks, flavors, toppings = get_menu()
    return render_template('forms.html', drinks=drinks, flavors=flavors, toppings=toppings)

@app.route("/list", methods=["GET"])
def list():
    if 'user' not in session:
        return redirect(url_for('login'))

    user = session['user']
    if user.get('rank') == 'admin':
        orders = get_orders()
    else:
        orders = get_orders(nickname=user['nickname']) 

    return render_template("list.html", orders=orders)

@app.route('/order/confirm', methods=['POST'])
def confirm_order():
    name = request.form.get('name')
    drink = request.form.get('drink')
    flavor = request.form.get('flavor')
    topping = request.form.get('topping')

    order = {
        'name': name,
        'drink': drink,
        'flavor': flavor,
        'topping': topping,
    }

    save_order(order)
    print(f"Order saved: {order}")

    return render_template('print.html', order=order)

@app.route('/registration',  methods=['GET', 'POST'])
def account_creation():
    if request.method == 'POST':
        nickname = request.form.get('username')
        mail = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        rank = request.form.get('rank')
        account = {
            'nickname': nickname,
            'email': mail,
            'password': password,
            'rank': rank,
        }
        if save_account(account):
            return render_template('create_acc.html', success='Account created! You can now log in.')
        else:
            return render_template('create_acc.html', error='Nickname already taken.')
    return render_template('create_acc.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nickname = request.form.get('username')
        password = request.form.get('password')
        user = check_login(nickname, password)
        if user.get('login'):
            session['user'] = {
                'nickname': user['nickname'],
                'email': user['email'],
                'rank': user['rank'],
            }
            return redirect(url_for('personal_page'))
        else:
            return render_template('login.html', error='Invalid nickname or password')
    return render_template('login.html')

@app.route('/personal_page', methods=['GET', 'POST'])
def personal_page():
    if 'user' not in session:
        return redirect(url_for('login'))
    user = session['user']
    return render_template('personal_page.html', user=user)

@app.route('/')
def home():
    print("Home route triggered!")
    return render_template('main_page.html')

#Python functions
def read_menu(filename: str) -> List[str]:
    names = []
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        names = file.readlines()
        names = [name.strip() for name in names]
    return names

def check_login(nickname, password):
    """
    Test‑only login – compares plain text passwords.
    Returns a dict with:
        'login': bool,
        'nickname': str (if successful),
        'email': str (if successful)
    """
    con = sqlite3.connect(ACCOUNTS_DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    cur.execute('SELECT nickname, email, password, rank FROM accounts WHERE nickname = ?', (nickname,))
    row = cur.fetchone()
    con.close()

    if row is None:
        return {'login': False}

    if row['password'] == password:
        return {
            'login': True,
            'nickname': row['nickname'],
            'email': row['email'],
            'password': row['password'],
            'rank': row['rank'],
        }
    else:
        return {'login': False}

def account_exists(nickname):
    """Return True if nickname already exists in accounts table."""
    con = sqlite3.connect(ACCOUNTS_DB)
    cur = con.cursor()
    cur.execute('SELECT 1 FROM accounts WHERE nickname = ?', (nickname,))
    exists = cur.fetchone() is not None
    con.close()
    return exists

def save_account(account):
    con = sqlite3.connect(ACCOUNTS_DB)
    #check if exsists
    if account_exists(account['nickname']):
        print(f"Account with nickname '{account['nickname']}' already exists.")
        return
    #Add new one
    rank = account.get('rank')
    if not rank:
        rank = 'user'
    cur = con.cursor()
    cur.execute('INSERT INTO accounts(nickname,email,password,rank) VALUES(?,?,?,?);',
                (account['nickname'], account['email'], account['password'], rank),)
    con.commit()
    return 

def save_order(order):
    con = sqlite3.connect(ORDERS_DB)
    cur = con.cursor()
    cur.execute('INSERT INTO orders(name,drink,flavor,topping) VALUES(?,?,?,?);',
                (order['name'], order['drink'], order['flavor'], order['topping']),)
    con.commit()
    return

def get_orders(nickname=None):
    con = sqlite3.connect(ORDERS_DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if nickname:
        cur.execute('SELECT * FROM orders WHERE name = ? ORDER BY rowid DESC', (nickname,))
    else:
        cur.execute('SELECT * FROM orders ORDER BY rowid DESC')
    rows = cur.fetchall()
    con.close()
    return rows

def get_menu():
    drinks = read_menu('drinks.txt')
    flavors = read_menu('flavors.txt')
    toppings = read_menu('toppings.txt')
    return drinks, flavors, toppings

#Start the server
if __name__ == '__main__':
    # Gather all files in templates/ and static/ recursively
    extra_dirs = ['templates', 'static']
    extra_files = []
    for extra_dir in extra_dirs:
        for dirname, _, filenames in os.walk(extra_dir):
            for filename in filenames:
                extra_files.append(os.path.join(dirname, filename))
    
    app.run( host='0.0.0.0', port=5000, debug=True, extra_files=extra_files)
    
    #serve(app, host='0.0.0.0', port=5000)