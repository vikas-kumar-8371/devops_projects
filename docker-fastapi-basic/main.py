# Basic DevOps Project - Step 1: Docker + FastAPI with CRUD
# Description: This is a minimal FastAPI app containerized using Docker that supports basic CRUD operations.

# -----------------------------
# 1. FastAPI Application 
# -----------------------------

from fastapi import FastAPI, HTTPException 
from pydantic import BaseModel

app = FastAPI() 

# In-memory database (dictionary)
db = {}

# Pydantic model for request/response class
class Item(BaseModel):
    name: str
    description: str

# CREATE an item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[item_id] = item
    return {"message": "Item created", "item": item}

# READ an item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return db[item_id]

# UPDATE an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = item
    return {"message": "Item updated", "item": item}

# DELETE an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"message": "Item deleted"}
