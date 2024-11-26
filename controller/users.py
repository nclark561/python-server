from fastapi import APIRouter, HTTPException, Depends
from dataAccess.users import get_user_da, create_user_da, update_user_da, delete_user_da
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from dataAccess.database import get_db
from sqlalchemy.exc import NoResultFound
from controller.posts import PostResponse

class UserBase(BaseModel):
    username: str
    
    class Config:
        orm_mode = True

class UserResponse(UserBase):
    id: str
    posts: list[PostResponse]

router = APIRouter()

@router.get("/users/{id}", response_model = UserResponse)
async def get_post(id, db: Session = Depends(get_db)):
    if id is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = get_user_da(id, db) 
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model = UserResponse)
async def create_post(user: UserBase, db: Session = Depends(get_db)):
    created_post = create_user_da(user.username, db)
    if created_post is None:
        raise HTTPException(status_code=400, detail="Failed to create post")
    return created_post

@router.put("/users/{id}", response_model = UserResponse)
async def update_post(id: str, user: UserBase, db: Session = Depends(get_db)):
    updated_post = update_user_da(id, user.username, db)
    if updated_post is None:
        raise HTTPException(status_code=400, detail="Failed to update post")
    return updated_post

@router.delete("/users/{id}")
async def delete_post(id: str, db: Session = Depends(get_db)):
    try:
        delete_user_da(id, db)
        return { "message": "post deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Post with ID not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return 