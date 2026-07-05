import requests
BASE_URL = "http://127.0.0.1:5000"

def view_all_items():
    try:
        response = requests.get(f"{BASE_URL}/inventory")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    items = response.json()

    if not items:
        print("No items in inventory.")
        return

    for item in items:
        print(f"[{item['id']}] {item['product_name']} — ${item['price']} — Stock: {item['stock_quantity']}")