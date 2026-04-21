import logging
import os
import sqlite3
from typing import *

from flask import Flask, render_template, request
from waitress import serve

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ORDERS_DB = os.path.join(BASE_DIR, "orders.db")

logging.basicConfig(level=logging.INFO)

con = sqlite3.connect(ORDERS_DB)
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS orders(name, drink, flavor, topping);")

app = Flask(__name__)


def read_menu(filename: str) -> List[str]:
    names = []
    filepath = os.path.join(BASE_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as file:
        names = file.readlines()
        names = [name.strip() for name in names]
    return names


@app.route("/order", methods=["GET"])
def show_order():
    drinks, flavors, toppings = get_menu()
    return render_template(
        "forms.html", drinks=drinks, flavors=flavors, toppings=toppings
    )


@app.route("/list", methods=["GET"])
def list():
    orders = get_orders()
    return render_template("list.html", orders=orders)


@app.route("/order/confirm", methods=["POST"])
def confirm_order():
    name = request.form.get("name")
    drink = request.form.get("drink")
    flavor = request.form.get("flavor")
    topping = request.form.get("topping")

    order = {
        "name": name,
        "drink": drink,
        "flavor": flavor,
        "topping": topping,
    }

    save_order(order)

    print(f"Order saved: {order}")

    return render_template("print.html", order=order)


def save_order(order):
    con = sqlite3.connect(ORDERS_DB)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO orders(name,drink,flavor,topping) VALUES(?,?,?,?);",
        (order["name"], order["drink"], order["flavor"], order["topping"]),
    )
    con.commit()
    return


def get_orders():
    con = sqlite3.connect(ORDERS_DB)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM orders;")
    rows = cur.fetchall()
    return rows


def get_menu():
    drinks = read_menu("drinks.txt")
    flavors = read_menu("flavors.txt")
    toppings = read_menu("toppings.txt")
    return drinks, flavors, toppings


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
    # app.run(debug=True)
