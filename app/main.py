from fastapi import Depends, FastAPI, Header, HTTPException
from .routers import items, users


app = FastAPI()


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


app.include_router(
    router=users.router,
    prefix='/users',
    tags=['users']
)

app.include_router(
    router=items.router,
    prefix='/items',
    tags=['items'],
    # dependencies=[Depends(get_token_header)],
    responses={404: {'description': 'Not found'}},
)

