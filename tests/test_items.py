import requests
from app.routers import items as item_routes
from app.routers.items import Item


BASE_URL = 'http://localhost:8000'


def test_items_api_get():
    response = requests.get(f'{BASE_URL}/items')
    assert response.status_code == 200
    items = [Item(**item) for item in response.json()]
    assert len(items) == 3


async def test_items_function_get():
    items = await item_routes.read_items()
    assert items[0].name == 'Item 1'
    assert len(items) == 3


def test_post_item():
    item_to_test = {
        "id": 4,
        "name": "item 4",
        "price": 4.99
    }

    response = requests.post(f'{BASE_URL}/items', json=item_to_test)
    assert response.status_code == 200
    assert response.json()['id'] == 4
