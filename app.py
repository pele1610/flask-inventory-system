from flask import Flask, jsonify, request
from data_store import get_all_items, get_item_by_id, add_item, update_item, delete_item

app = Flask(__name__)

@app.route("/inventory", methods=["GET"])
def get_inventory():
    items = get_all_items()
    return jsonify(items), 200