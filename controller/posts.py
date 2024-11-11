from fastapi import APIRouter, HTTPException, Depends
from dataAccess.posts import get_posts, get_post, create_post, update_post, delete_post
from dataAccess.models import Post
from dataAccess.database import get_db
from sqlalchemy.orm import Session


router = APIRouter()

@router.get("/posts")
async def get_posts(db: Session = Depends(get_db)):
    print('i ran')
    try:
        posts = get_posts(db)
        if posts is None:
            return []
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/{id}")
async def get_post(id: str, db: Session = Depends(get_db)):
    post = get_post(id, db) 
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts")
async def create_post(post: Post, db: Session = Depends(get_db)):
    created_post = create_post(post, db)
    if created_post is None:
        raise HTTPException(status_code=400, detail="Failed to create post")
    return created_post

@router.put("/posts/{id}")
async def update_post(id: str, post: Post, db: Session = Depends(get_db)):
    updated_post = update_post(id, post, db)
    if updated_post is None:
        raise HTTPException(status_code=400, detail="Failed to update post")
    return updated_post

@router.delete("/posts/{id}")
async def delete_post(id: str, db: Session = Depends(get_db)):
    deleted_post = delete_post(id, db)
    if deleted_post is None:
        raise HTTPException(status_code=400, detail="Failed to delete post")
    return deleted_post