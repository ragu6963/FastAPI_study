from fastapi import APIRouter
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


router = APIRouter(
    prefix="/path",
    tags=["path"],
)


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@router.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """값 사전 정의(Enum 클래스)"""
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@router.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """경로를 포함한 경로 매개변수

    Args:
        file_path (str): 경로(파일 등)

    """
    return {"file_path": file_path}
