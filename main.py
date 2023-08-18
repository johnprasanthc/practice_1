from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name: str = 'name'
    email: str= 'email'
    

@app.get("/")
async def print_data(data:Data):
    print(data)
    return {"message":"Hello world"}
