# testing/test_api.py

import pytest
import app
import data_store


@pytest.fixture(autouse=True)
def reset_inventory():
    data_store.inventory = [
        {
            "id": 1,
            "barcode": "111",
            "product_name": "Test Item",
            "brand": "Test Brand",
            "ingredients_text": "Test ingredients",
            "price": 5.00,
            "stock_quantity": 10
        }
    ]
    data_store.next_id = 2
    yield


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as test_client:
        yield test_client


def test_get_all_items(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 1
    assert data[0]["product_name"] == "Test Item"


def test_get_item_found(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1


def test_get_item_not_found(client):
    response = client.get("/inventory/999")
    assert response.status_code == 404


def test_create_item(client):
    response = client.post("/inventory", json={
        "barcode": "333",
        "product_name": "New Product",
        "price": 12.50,
        "stock_quantity": 8
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["id"] == 2
    assert data["product_name"] == "New Product"


def test_create_item_missing_fields(client):
    response = client.post("/inventory", json={"product_name": "Incomplete"})
    assert response.status_code == 400


def test_update_item(client):
    response = client.patch("/inventory/1", json={"price": 99.99})
    assert response.status_code == 200
    data = response.get_json()
    assert data["price"] == 99.99


def test_update_item_not_found(client):
    response = client.patch("/inventory/999", json={"price": 99.99})
    assert response.status_code == 404


def test_delete_item(client):
    response = client.delete("/inventory/1")
    assert response.status_code == 200


def test_delete_item_not_found(client):
    response = client.delete("/inventory/999")
    assert response.status_code == 404