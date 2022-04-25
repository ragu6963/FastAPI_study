from fastapi import APIRouter
from typing import Optional


router = APIRouter(
    prefix="/query",
    tags=["query"],
)


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """쿼리 매개변수
    경로 매개변수가 아닌 매개변수는 쿼리 매개변수로 해석한다.
    """
    return fake_items_db[skip : skip + limit]


@router.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    """선택적 매개변수
    Optional을 통해 선택적 매개변수를 선언할 수 있다.
    """
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    """여러개의 경로 매개변수와 쿼리 매개변수를 선언할 수 있다."""
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    """필수 쿼리 매개변수
    기본값 없이 매개변수를 선언하면 필수 매개변수로 해석한다.
    여기서 needy 는 str 형 필수 매개변수이다.
    """
    item = {"item_id": item_id, "needy": needy}
    return item
