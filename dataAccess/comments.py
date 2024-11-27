from dataAccess.models import Comment
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

def get_comments_da(db: Session):
    return db.query(Comment).all()

def get_comment_da(id, db: Session):
    return db.query(Comment).filter(Comment.id == id).first()

def create_comment_da(content: str, post_id, owner_id, db: Session):
    new_comment = Comment(content=content, owner_id=owner_id, post_id=post_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def update_comment_da(id, content: str, db: Session):
    comment = db.query(Comment).filter(Comment.id == id).first()
    if comment is None:
        raise NoResultFound("post not found")
    comment.content = content
    db.commit()
    db.refresh(comment)
    return comment

def delete_comment_da(id, db: Session):
    comment = db.query(Comment).filter(Comment.id == id).first()
    if comment is None:
        raise NoResultFound("post not found")
    db.delete(comment)
    db.commit()
    return