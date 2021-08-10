from fastapi import Depends, FastAPI

from app.api.v1.api import api_router
from app.api.deps import oauth2_scheme

app = FastAPI(title='FastAPI test')


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

app.include_router(api_router)
