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
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_all_items()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()