from fastapi import APIRouter, HTTPException, Depends
from dataAccess.posts import get_posts_da, get_post_da, create_post_da, update_post_da, delete_post_da
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from dataAccess.database import get_db
from sqlalchemy.exc import NoResultFound

class PostBase(BaseModel):
    content: str
    owner_id: str
    
    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id: str
    date: datetime

router = APIRouter()

@router.get("/posts", response_model = list[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    try:
        posts = get_posts_da(db)
        if posts is None:
            return { posts: [] }
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/posts/{id}", response_model = PostResponse)
async def get_post(id, db: Session = Depends(get_db)):
    post = get_post_da(id, db) 
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.post("/posts", response_model = PostResponse)
async def create_post(post: PostBase, db: Session = Depends(get_db)):
    created_post = create_post_da(post.content, post.owner_id, db)
    if created_post is None:
        raise HTTPException(status_code=400, detail="Failed to create post")
    return created_post

@router.put("/posts/{id}", response_model = PostResponse)
async def update_post(id: str, post: PostBase, db: Session = Depends(get_db)):
    updated_post = update_post_da(id, post.content, db)
    if updated_post is None:
        raise HTTPException(status_code=400, detail="Failed to update post")
    return updated_post

@router.delete("/posts/{id}")
async def delete_post(id: str, db: Session = Depends(get_db)):
    try:
        delete_post_da(id, db)
        return { "message": "post deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Post with ID not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return 