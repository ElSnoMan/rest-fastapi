from typing import List
from fastapi import APIRouter, HTTPException
from app.models.item import Item, items_db

router = APIRouter()


@router.get('/', response_model=List[Item])
async def read_items():
    return [Item(**item) for item in items_db]


@router.get('/{item_id}', response_model=Item)
async def read_item(item_id: str):
    for item in [Item(**item) for item in items_db]:
        if item_id == str(item.id):
            return item
    raise HTTPException(status_code=404, detail='Item not found')


@router.put(
    path='/{item_id}',
    tags=['custom'],
    responses={403: {"description": "Operation forbidden"}},
    response_model=Item
)
async def update_item(item_id: int, item: Item):
    item_found = next((index, _item) for index, _item in enumerate(items_db) if _item['id'] == item_id)
    result = {'id': item_id, **item.dict()}
    items_db[item_found[0]] = result
    return result


@router.post('/')
async def create_item(item: Item):
    items_db.append(item.dict())
    return item
