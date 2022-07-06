from app import app
from flask import render_template
from models.order_list import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="Records Orders", all_orders=orders)


@app.route("/orders/<int:order_number>")
def index1(order_number):
    return render_template(
        "order.html", title="Customer Order", order=orders[order_number]
    )
