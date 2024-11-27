from fastapi import APIRouter, HTTPException, Depends
from dataAccess.comments import get_comments_da, get_comment_da, create_comment_da, update_comment_da, delete_comment_da
from pydantic import BaseModel
from datetime import datetime
from sqlalchemy.orm import Session
from dataAccess.database import get_db
from sqlalchemy.exc import NoResultFound

class CommentBase(BaseModel):
    content: str
    owner_id: str
    post_id: str
    
    class Config:
        orm_mode = True

class CommentResponse(CommentBase):
    id: str
    date: datetime

router = APIRouter()

@router.get("/comments", response_model = list[CommentResponse])
async def get_comments(db: Session = Depends(get_db)):
    try:
        comments = get_comments_da(db)
        if comments is None:
            return { comments: [] }
        return comments
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/comments/{id}", response_model = CommentResponse)
async def get_comment(id, db: Session = Depends(get_db)):
    comment = get_comment_da(id, db) 
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.post("/comments", response_model = CommentResponse)
async def create_comment(comment: CommentBase, db: Session = Depends(get_db)):
    created_comment = create_comment_da(comment.content, comment.post_id, comment.owner_id, db)
    if created_comment is None:
        raise HTTPException(status_code=400, detail="Failed to create comment")
    return created_comment

@router.put("/comments/{id}", response_model = CommentResponse)
async def update_comment(id: str, comment: CommentBase, db: Session = Depends(get_db)):
    updated_comment = update_comment_da(id, comment.content, db)
    if updated_comment is None:
        raise HTTPException(status_code=400, detail="Failed to update comment")
    return updated_comment

@router.delete("/comments/{id}")
async def delete_comment(id: str, db: Session = Depends(get_db)):
    try:
        delete_comment_da(id, db)
        return { "message": "comment deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Comment with ID not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return 