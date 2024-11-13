from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from dataAccess.database import Base
from datetime import datetime, timezone
from cuid import cuid

class Post(Base):
    __tablename__ = 'posts'

    id = Column(String, primary_key=True, default=lambda: cuid())
    content = Column(String)
    date = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(String, ForeignKey('users.id'))
    owner = relationship('User', back_populates='posts')
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True, default=lambda: cuid())
    username = Column(String)
    posts = relationship('Post', back_populates='owner')