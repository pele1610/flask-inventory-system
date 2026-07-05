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


def main():
    while True:
        print("\n--- Inventory CLI ---")
        print("1. View all items")
        print("2. View one item")
        print("3. Add new item")
        print("4. Update an item")
        print("5. Delete an item")
        print("6. Find item on API (by barcode)")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_items()
        elif choice == "2":
            view_one_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
            update_item()
        elif choice == "5":
            delete_item()
        elif choice == "6":
            lookup_product()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

def view_one_item():
    item_id = input("Enter item ID: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("Invalid ID — must be a number.")
        return

    try:
        response = requests.get(f"{BASE_URL}/inventory/{item_id}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if response.status_code == 404:
        print("Item not found.")
        return

    item = response.json()
    print(f"[{item['id']}] {item['product_name']}")
    print(f"  Brand: {item['brand']}")
    print(f"  Price: ${item['price']}")
    print(f"  Stock: {item['stock_quantity']}")
    print(f"  Barcode: {item['barcode']}")
    print(f"  Ingredients: {item['ingredients_text']}")

def add_item():
    print("Enter new item details:")
    barcode = input("Barcode: ")
    product_name = input("Product name: ")
    brand = input("Brand: ")
    ingredients_text = input("Ingredients: ")

    try:
        price = float(input("Price: "))
        stock_quantity = int(input("Stock quantity: "))
    except ValueError:
        print("Price must be a number and stock quantity must be a whole number.")
        return

    payload = {
        "barcode": barcode,
        "product_name": product_name,
        "brand": brand,
        "ingredients_text": ingredients_text,
        "price": price,
        "stock_quantity": stock_quantity
    }

    try:
        response = requests.post(f"{BASE_URL}/inventory", json=payload)
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if response.status_code == 201:
        new_item = response.json()
        print(f"Item added successfully with ID {new_item['id']}.")
    else:
        print(f"Failed to add item: {response.json().get('error')}")
def update_item():
    item_id = input("Enter item ID to update: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("Invalid ID — must be a number.")
        return

    print("Leave blank to keep current value.")
    price_input = input("New price: ")
    stock_input = input("New stock quantity: ")

    payload = {}

    if price_input.strip():
        try:
            payload["price"] = float(price_input)
        except ValueError:
            print("Price must be a number.")
            return

    if stock_input.strip():
        try:
            payload["stock_quantity"] = int(stock_input)
        except ValueError:
            print("Stock quantity must be a whole number.")
            return

    if not payload:
        print("Nothing to update.")
        return

    try:
        response = requests.patch(f"{BASE_URL}/inventory/{item_id}", json=payload)
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if response.status_code == 404:
        print("Item not found.")
    elif response.status_code == 200:
        print("Item updated successfully.")
    else:
        print(f"Update failed: {response.json().get('error')}")

def delete_item():
    item_id = input("Enter item ID to delete: ")

    try:
        item_id = int(item_id)
    except ValueError:
        print("Invalid ID — must be a number.")
        return

    confirm = input(f"Are you sure you want to delete item {item_id}? (y/n): ")
    if confirm.lower() != "y":
        print("Cancelled.")
        return

    try:
        response = requests.delete(f"{BASE_URL}/inventory/{item_id}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if response.status_code == 404:
        print("Item not found.")
    elif response.status_code == 200:
        print("Item deleted successfully.")
    else:
        print(f"Delete failed: {response.json().get('error')}")

def lookup_product():
    barcode = input("Enter barcode to look up: ")

    try:
        response = requests.get(f"{BASE_URL}/lookup/{barcode}")
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if response.status_code == 404:
        print("Product not found on OpenFoodFacts.")
        return

    product = response.json()
    print(f"Found: {product['product_name']}")
    print(f"  Brand: {product['brand']}")
    print(f"  Ingredients: {product['ingredients_text']}")

    add_choice = input("Add this to inventory? (y/n): ")
    if add_choice.lower() != "y":
        print("Not added.")
        return

    try:
        price = float(input("Price: "))
        stock_quantity = int(input("Stock quantity: "))
    except ValueError:
        print("Price must be a number and stock quantity must be a whole number.")
        return

    payload = {
        "barcode": product["barcode"],
        "product_name": product["product_name"],
        "brand": product["brand"],
        "ingredients_text": product["ingredients_text"],
        "price": price,
        "stock_quantity": stock_quantity
    }

    try:
        add_response = requests.post(f"{BASE_URL}/inventory", json=payload)
    except requests.exceptions.ConnectionError:
        print("Could not connect to the server. Is it running?")
        return

    if add_response.status_code == 201:
        new_item = add_response.json()
        print(f"Added to inventory with ID {new_item['id']}.")
    else:
        print(f"Failed to add: {add_response.json().get('error')}")

if __name__ == "__main__":
    main()