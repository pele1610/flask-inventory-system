# Flask Inventory Management System

A REST API for managing retail inventory, with OpenFoodFacts integration for product lookup, and a CLI client.

## Setup

```bash
git clone <your-repo-url>
cd flask-inventory-system-v2
pipenv install
pipenv install pytest pytest-mock --dev
pipenv shell
```

## Running the API

```bash
python3 app.py
```

Server runs at `http://127.0.0.1:5000`.

## Running the CLI

In a separate terminal (with the API running):

```bash
python3 cli.py
```

## Running tests

```bash
pytest testing/ -v
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|--------------|
| GET | /inventory | Fetch all items |
| GET | /inventory/<id> | Fetch a single item |
| POST | /inventory | Add a new item (requires barcode, product_name, price, stock_quantity) |
| PATCH | /inventory/<id> | Update an item (partial update) |
| DELETE | /inventory/<id> | Remove an item |
| GET | /lookup/<barcode> | Fetch product details from OpenFoodFacts |

### Example: create an item

```bash
curl -X POST http://127.0.0.1:5000/inventory \
  -H "Content-Type: application/json" \
  -d '{"barcode": "3017620422003", "product_name": "Nutella", "price": 4.99, "stock_quantity": 20}'
```

## CLI Usage

The CLI presents a menu: