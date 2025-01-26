from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Define a model for an Item
class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

# In-memory storage for the items
items = {}

# Create an item
@app.post("/items/", status_code=201)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail="Item with this ID already exists.")
    items[item.id] = item
    return {"message": "Item created successfully", "item": item}

# Read an item by ID
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found.")
    return items[item_id]

# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found.")
    items[item_id] = updated_item
    return {"message": "Item updated successfully", "item": updated_item}

# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found.")
    del items[item_id]
    return {"message": "Item deleted successfully"}

# List all items
@app.get("/items/")
def list_items():
    return {"items": list(items.values())}

