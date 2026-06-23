from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items = []

@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Item:
    """Create a new item in the inventory."""
    try:
        items.append(item)
        return item
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/', response_model=List[Item])
async def read_items() -> List[Item]:
    """Retrieve all items from the inventory."""
    try:
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/items/{item_id}', response_model=Item)
async def read_item(item_id: int) -> Item:
    """Retrieve an item by its ID."""
    try:
        for item in items:
            if item.id == item_id:
                return item
        raise HTTPException(status_code=404, detail='Item not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete('/items/{item_id}', response_model=Item)
async def delete_item(item_id: int) -> Item:
    """Delete an item by its ID."""
    try:
        for index, item in enumerate(items):
            if item.id == item_id:
                return items.pop(index)
        raise HTTPException(status_code=404, detail='Item not found')
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))