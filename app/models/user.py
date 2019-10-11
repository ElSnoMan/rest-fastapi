from typing import List
from pydantic import BaseModel
from app.models.item import Item


class User(BaseModel):
    email: str
    username: str
    password: str
    cartItems: List[Item] = None


users_db = [
    {
        'id': 0,
        'email': 'me@test.com',
        'username': 'me',
        'password': 'password'
    },
    {
        'id': 1,
        'email': 'user1@test.com',
        'username': 'fizz',
        'password': '1234!'
    },
    {
        'id': 2,
        'email': 'user2@test.com',
        'username': 'buzz',
        'password': '1234!',
        'cartItems': [
            {
                'id': 1,
                'name': 'Item 1',
                'price': 5.00
            }
        ]
    },
    {
        'id': 3,
        'email': 'user3@test.com',
        'username': 'fizz_buzz',
        'password': '1234!',
        'cartItems': [
            {
                'id': 1,
                'name': 'Item 1',
                'price': 5.00
            },
            {
                'id': 2,
                'name': 'Item 2',
                'price': 10.00,
                'isOffer': True
            }
        ]
    }
]
