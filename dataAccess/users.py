from dataAccess.models import User
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import NoResultFound

def get_user_da(id: str, db: Session):
    return db.query(User).filter(User.id == id).options(joinedload(User.posts)).first()

def create_user_da(username: str, db: Session):
    new_user = User(username=username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user_da(id: str, username: str, db: Session):
    updated_user = db.query(User).filter(User.id == id).first()
    if updated_user is None:
        raise NoResultFound("user not found")
    updated_user.username = username
    db.commit()
    db.refresh(updated_user)
    return updated_user

def delete_user_da(id: str, db: Session):
    deleted_user = db.query(User).filter(User.id == id).first()
    if deleted_user is None:
        raise NoResultFound('user not found')
    db.delete(deleted_user)
    db.commit()
    return 