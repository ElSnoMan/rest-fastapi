import requests
from app.routers import users
from app.models.user import User


BASE_URL = 'http://localhost:8000'


def test_items_api_get():
    username = 'yehboii'
    response = requests.get(f'{BASE_URL}/users/{username}')
    assert response.status_code == 200

    user = next([User(**user) for user in response.json()])
    assert user.username == username
    assert user.cartItems is not None


async def test_users_function_get():
    username = 'yehboii'
    user = await users.read_user('yehboii')
    assert user.username == username
