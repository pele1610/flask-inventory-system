# external_api.py

import requests

OPENFOODFACTS_URL = "https://world.openfoodfacts.org/api/v2/product/{}.json"
HEADERS = {"User-Agent": "InventoryApp/1.0 (contact@example.com)"}



def fetch_product_by_barcode(barcode):
    
    url = OPENFOODFACTS_URL.format(barcode)

    try:
       response = requests.get(url, headers=HEADERS, timeout=5) 
    except requests.exceptions.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    product = data.get("product", {})

    return {
        "barcode": barcode,
        "product_name": product.get("product_name", ""),
        "brand": product.get("brands", ""),
        "ingredients_text": product.get("ingredients_text", "")
    }
