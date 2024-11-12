from dataAccess.models import Post
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

def get_posts_da(db: Session):
    return db.query(Post).all()

def get_post_da(id, db: Session):
    return db.query(Post).filter(Post.id == id).first()

def create_post_da(content: str, db: Session):
    new_post = Post(content=content)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post_da(id, content: str, db: Session):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise NoResultFound("post not found")
    post.content = content
    db.commit()
    db.refresh(post)
    return post

def delete_post_da(id, db: Session):
    post = db.query(Post).filter(Post.id == id).first()
    if post is None:
        raise NoResultFound("post not found")
    db.delete(post)
    db.commit()
    return