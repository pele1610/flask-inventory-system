inventory = [
    {
        "id": 1,
        "barcode": "3017620422003",
        "product_name": "Organic Almond Milk",
        "brand": "Silk",
        "ingredients_text": "Filtered water, almonds, cane sugar",
        "price": 4.99,
        "stock_quantity": 25
    },
    {
        "id": 2,
        "barcode": "5449000000996",
        "product_name": "Coca-Cola Classic",
        "brand": "Coca-Cola",
        "ingredients_text": "Carbonated water, sugar, caramel color",
        "price": 1.50,
        "stock_quantity": 100
    }
]

next_id =3


def get_all_items():
    """Return the entire inventory list."""
    return inventory


def get_item_by_id(item_id):
    """
    Find and return a single item matching item_id.
    Returns None if no item has that id.
    """
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None