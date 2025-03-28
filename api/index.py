from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI on Vercel!"}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from API route"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is item " + str(item_id)}

# This handler is required for Vercel serverless deployment
handler = Mangum(app)