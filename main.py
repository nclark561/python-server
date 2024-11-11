from fastapi import FastAPI
from controller import items, posts

app = FastAPI()

app.include_router(items.router)
app.include_router(posts.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}