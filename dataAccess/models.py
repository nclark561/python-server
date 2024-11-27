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
    comments = relationship('Comment', back_populates='post')
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(String, primary_key=True, default=lambda: cuid())
    username = Column(String)
    posts = relationship('Post', back_populates='owner')
    comments = relationship('Comment', back_populates='owner')
    
class Comment(Base):
    __tablename__ = 'comments'

    id = Column(String, primary_key=True, default=lambda: cuid())
    content = Column(String)
    date = Column(DateTime, default=datetime.now(timezone.utc))
    owner_id = Column(String, ForeignKey('users.id'))
    owner = relationship('User', back_populates='comments')
    post_id = Column(String, ForeignKey('posts.id'))
    post = relationship('Post', back_populates='comments')