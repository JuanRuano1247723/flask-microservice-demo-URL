from flask import Flask, json, jsonify, request
import logging
import requests


app = Flask(__name__)


@app.route('/orders', methods=['GET'])
def orders():
    count = request.args.get('count')
    data = requests.get('http://demo_orders:5000/allOrders').json()
    if count:
        return jsonify(data[:int(count)]), 200
    else:
        return jsonify(data), 200


@app.route('/detail/<int:order_id>', methods=['GET'])
def detail(order_id):
    order = requests.get(f'http://demo_orders:5000/order/{order_id}').json()
    
    items = []
    for item_id in order.get('items', []):
        item = requests.get(f'http://demo_items:5000/item/{item_id}').json()
        items.append(item)
    
    order['items'] = items
    return jsonify(order), 200


@app.route('/custSearch/<string:name>', methods=['GET'])
def cust_search(name):
    payload = {'name': name}
    data = requests.post('http://demo_orders:5000/custSearch', json=payload).json()
    return jsonify(data), 200


if __name__ == '__main__':
    app.logger.setLevel(logging.INFO)
    app.run(debug=True, host='0.0.0.0')
