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
    return inventory


def get_item_by_id(item_id):
    for item in inventory:
        if item["id"] == item_id:
            return item
    return None


def add_item(data):
    
    global next_id

    new_item = {
        "id": next_id,
        "barcode": data.get("barcode", ""),
        "product_name": data.get("product_name", ""),
        "brand": data.get("brand", ""),
        "ingredients_text": data.get("ingredients_text", ""),
        "price": data.get("price", 0.0),
        "stock_quantity": data.get("stock_quantity", 0)
    }

    inventory.append(new_item)
    next_id += 1

    return new_item

def update_item(item_id, data):
    item = get_item_by_id(item_id)
    if item is None:
        return None

    for key in ["barcode", "product_name", "brand", "ingredients_text", "price", "stock_quantity"]:
        if key in data:
            item[key] = data[key]

    return item


def delete_item(item_id):
    global inventory
    item = get_item_by_id(item_id)
    if item is None:
        return False

    inventory = [i for i in inventory if i["id"] != item_id]
    return True
