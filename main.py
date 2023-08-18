from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    name: str
    

@app.get("/")
async def print_data(data:Data):
    print(data)