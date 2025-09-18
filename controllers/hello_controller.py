from fastapi import APIRouter
from models.hello import HelloResponse

router = APIRouter()


@router.get("/", response_model=HelloResponse)
def hello():
    return HelloResponse(message="Hello, world im yu!")
