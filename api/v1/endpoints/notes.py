from fastapi import APIRouter,Request
from services.notes_service import get_all_notes

router = APIRouter()

@router.get("/")
def homepage():
    return {"Hello": "World"}


# @router.get("/items")
# def read_all_item(request: Request):
#     all_nottes=get_all_notes()
#     return {"item_id": item_id, "q": q}