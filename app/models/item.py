from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    price: float
    isOffer: bool = None


items_db = [
    {
        'id': 1,
        'name': 'Item 1',
        'price': 5.00
    },
    {
        'id': 2,
        'name': 'Item 2',
        'price': 10.34,
        'isOffer': False
    },
    {
        'id': 3,
        'name': 'Item 3',
        'price': 19.99,
        'isOffer': True
    }
]
