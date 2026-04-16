from flask import Flask, render_template, request
from waitress import serve
import logging
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_FILE = os.path.join(BASE_DIR, 'orders.json')

logging.basicConfig(level=logging.INFO)

from typing import *
app = Flask(__name__)

def read_menu(filename: str) -> List[str]:
    names = []
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as file:
        names = file.readlines()
        names = [name.strip() for name in names]
    return names

@app.route('/order', methods = ['GET'])
def show_order():
    drinks, flavors, toppings = get_menu()
    return render_template('forms.html', drinks=drinks, flavors=flavors, toppings=toppings)

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
def load_orders():
    import json 
    filepath = ORDERS_FILE
    with open(filepath) as fl:
        try:
            return json.load(fl)
        except json.JSONDecodeError:
            return []
    
def save_order(order):
    import json
    orders = load_orders()
    orders.append(order)
    filepath = ORDERS_FILE
    with open(filepath, 'w') as file:
        json.dump(orders, file, indent=4)

def get_menu():
    drinks = read_menu('drinks.txt')
    flavors = read_menu('flavors.txt')
    toppings = read_menu('toppings.txt')
    return drinks, flavors, toppings

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
    #app.run(debug=True)