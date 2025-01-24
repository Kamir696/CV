from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

cors_policy = {
    "allow_origins": ["*"],
    "allow_credentials": True,
    "allow_methods": ["GET", "POST"],
    "allow_headers": ["*"],
}

app.add_middleware(
    CORSMiddleware,
    **cors_policy
)

#@app.get("/")
#def read_root():
#   return {"Message": "HOLA CLASE DE MATE"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": f"This is a description {item_id}"}

@app.post("/items/5")
def create_item():
    return {"Message": "Item created successfully"}