from flask import Flask, render_template, request
from waitress import serve
from typing import *
import logging
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_DB = os.path.join(BASE_DIR, 'orders.db')
ACCOUNT_DB = os.path.join(BASE_DIR, 'accounts.db')

logging.basicConfig(level=logging.INFO)

#DataBases
con = sqlite3.connect(ORDERS_DB)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS orders(name, drink, flavor, topping);')
con = sqlite3.connect(ACCOUNT_DB)
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS accounts(nickname, name, email, password);')

#Flask app
app = Flask(__name__)

@app.route('/order', methods = ['GET'])
def show_order():
    drinks, flavors, toppings = get_menu()
    return render_template('forms.html', drinks=drinks, flavors=flavors, toppings=toppings)

@app.route("/list", methods=["GET"])
def list():
    orders = get_orders()
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
    return render_template('create_acc.html')

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

def save_order(order):
    con = sqlite3.connect(ORDERS_DB)
    cur = con.cursor()
    cur.execute('INSERT INTO orders(name,drink,flavor,topping) VALUES(?,?,?,?);',
                (order['name'], order['drink'], order['flavor'], order['topping']),)
    con.commit()
    return

def get_orders():
    con = sqlite3.connect(ORDERS_DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM orders;')
    rows = cur.fetchall()
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