from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from FastAPI on Vercel!"}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from the API"}

@app.get("/api/items/{item_id}")
async def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# For local testing
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
