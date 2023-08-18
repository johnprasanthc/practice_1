from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Sample data
items = [
    {"id": 1, "name": "Item 1","count":1},
    {"id": 2, "name": "Item 2","count":2},
    {"id": 3, "name": "Item 3","count":7},
]
next_item_id = len(items)+1

class Item(BaseModel):
    name: str
    count:int=1

@app.get("/")
async def read_root():
    return {"message": "Welcome to the API Test"}

@app.get("/items")
async def read_items():
    return items

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post("/items")
async def create_item(item: Item):
    global next_item_id
    print(item)
    new_item = {"id": next_item_id, "name": item.name+" "+str(next_item_id),"count":item.count}
    items.append(new_item)
    next_item_id += 1
    return new_item

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: Item):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item["name"] = updated_item.name+" "+str(item_id)
    item["count"]=updated_item.count
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted"}
