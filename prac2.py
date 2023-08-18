from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import uvicorn
#uvicorn.run(app, host="127.0.0.1", port=3000)

app=FastAPI()

class Item(BaseModel):
    name:str

items=[
    {'id':1,"name":'Item 1'},
    {"id":2,"name": "Item 2"},
    {"id":3,"name":"Item 3"}
]

next_item_id = len(items)+1

@app.get("/")
async def read_root():
    return {"message":"Welcome to the API Test"}

@app.get('/items')
async def read_items():
    return items

@app.post('/items')
async def create_item(item:Item):
    print(item)
    global next_item_id
    new_item={"id":next_item_id,"name":item.name}
    next_item_id+=1
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}")
async def update_item(item_id:int,updated_item:Item):
    item = next((item for item in items if item["id"] == item_id), None)
    if item==None:
        raise HTTPException(status_code=404,detail="Item not found")
    item["name"]=updated_item.name
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id:int):
    global items
    items=[item for item in items if item['id']!=item_id]
    return {"message":"Item deleted"}