
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Konfiguracja CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Możesz tu wpisać konkretne domeny np. ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ItemDetails(BaseModel):
    brand: str
    catalog: int
    price: float
    size: int
    status: str


@app.get("/item/{item_id}")
def read_item(item_id: int):
    # Return a mock item for demonstration
    return {
        "item_id": item_id,
        "brand": "Example Brand",
        "catalog": 12345,
        "price": 99.99,
        "size": 42,
        "status": "available"
    }

@app.post("/vinted/items")
def create_item(item: ItemDetails):
    return item
