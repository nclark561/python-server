from fastapi import FastAPI
from controller import items, posts, users, comments

app = FastAPI()

app.include_router(items.router)
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(comments.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}