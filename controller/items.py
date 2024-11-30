from fastapi import APIRouter, HTTPException

router = APIRouter()

items = [{"id": 1, "name": "Item 1", "description": "Description 1"}, {"id": 2, "name": "Item 2", "description": "Description 2"}, {"id": 3, "name": "Item 3", "description": "Description 3"}]

@router.get("/items")
async def get_items():
    return items

@router.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id >= 1 and item_id < len(items) + 1:
        return items[item_id - 1]
    else:
        raise HTTPException(status_code=404, detail="Item not found.")
@router.get("/thanksgiving")    
async def get_thanksgiving():
    return "Happy Thanksgiving!"
