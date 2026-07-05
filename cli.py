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
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_items()
        elif choice == "2":
            view_one_item()
        elif choice == "3":
            add_item()
        elif choice == "4":
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


if __name__ == "__main__":
    main()