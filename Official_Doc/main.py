# Python 타입 표시 모듈
from typing import Optional
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()


# GET method
@app.get("/")
def read_root():
    return {
        "Hello": "World",
    }


# item_id : 경로 매개변수
# q : 선택적(Optional) 쿼리 매개변수
# :int 는 타입 표시 및 검증
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q,
    }


# 매개변수로 경로(path) 받기
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# 다중 경로, 쿼리 매개변수
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
