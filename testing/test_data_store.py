# testing/test_data_store.py

import pytest
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


def test_get_all_items():
    items = data_store.get_all_items()
    assert len(items) == 1
    assert items[0]["product_name"] == "Test Item"


def test_get_item_by_id_found():
    item = data_store.get_item_by_id(1)
    assert item is not None
    assert item["id"] == 1


def test_get_item_by_id_not_found():
    item = data_store.get_item_by_id(999)
    assert item is None


def test_add_item():
    new_item = data_store.add_item({
        "barcode": "222",
        "product_name": "New Item",
        "brand": "New Brand",
        "ingredients_text": "New ingredients",
        "price": 9.99,
        "stock_quantity": 5
    })
    assert new_item["id"] == 2
    assert len(data_store.get_all_items()) == 2


def test_update_item_found():
    updated = data_store.update_item(1, {"price": 7.50})
    assert updated["price"] == 7.50
    assert updated["product_name"] == "Test Item"


def test_update_item_not_found():
    updated = data_store.update_item(999, {"price": 7.50})
    assert updated is None


def test_delete_item_found():
    result = data_store.delete_item(1)
    assert result is True
    assert data_store.get_item_by_id(1) is None


def test_delete_item_not_found():
    result = data_store.delete_item(999)
    assert result is False