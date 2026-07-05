from flask import Flask, jsonify, request
from requests import get
from data_store import get_all_items, get_item_by_id, add_item, update_item, delete_item

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_inventory():
    items = get_all_items()
    return jsonify(items), 200


@app.route("/inventory/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = get_item_by_id(item_id)
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    return jsonify(item), 200


@app.route("/inventory", methods=["POST"])
def create_item():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400
    

    required_fields = ["barcode", "product_name", "price", "stock_quantity"]
    missing =[f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"missing required fields: {missing}"}), 400
    
    
    new_item =add_item(data)
    return jsonify(new_item), 201