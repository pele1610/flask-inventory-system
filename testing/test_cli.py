# testing/test_cli.py

from unittest.mock import patch, Mock
import cli


@patch("cli.requests.get")
def test_view_all_items(mock_get, capsys):
    mock_response = Mock()
    mock_response.json.return_value = [
        {"id": 1, "product_name": "Item A", "price": 5.0, "stock_quantity": 3}
    ]
    mock_get.return_value = mock_response

    cli.view_all_items()

    captured = capsys.readouterr()
    assert "Item A" in captured.out


@patch("cli.requests.get")
def test_view_all_items_empty(mock_get, capsys):
    mock_response = Mock()
    mock_response.json.return_value = []
    mock_get.return_value = mock_response

    cli.view_all_items()

    captured = capsys.readouterr()
    assert "No items in inventory." in captured.out


@patch("cli.input", side_effect=["abc"])
def test_view_one_item_invalid_id(mock_input, capsys):
    cli.view_one_item()

    captured = capsys.readouterr()
    assert "Invalid ID" in captured.out


@patch("cli.requests.get")
@patch("cli.input", side_effect=["999"])
def test_view_one_item_not_found(mock_input, mock_get, capsys):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    cli.view_one_item()

    captured = capsys.readouterr()
    assert "Item not found." in captured.out


@patch("cli.requests.post")
@patch("cli.input", side_effect=["111", "Test Product", "Brand", "Ingredients", "5.00", "10"])
def test_add_item_success(mock_input, mock_post, capsys):
    mock_response = Mock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"id": 5, "product_name": "Test Product"}
    mock_post.return_value = mock_response

    cli.add_item()

    captured = capsys.readouterr()
    assert "Item added successfully with ID 5." in captured.out