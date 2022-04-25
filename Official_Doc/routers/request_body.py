from fastapi import APIRouter

from pydantic import BaseModel
from typing import Optional

router = APIRouter(
    prefix="/request",
    tags=["request"],
)


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@router.post("/items/")
async def create_item(item: Item):
    return item


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, query: Optional[str] = None):
    """request body, path parameter, query parameter 조합"""
    result = {"item_id": item_id, **item.dict()}
    if query:
        result.update({"query": query})
    return result
