from sqlalchemy import Column, String, DateTime
from dataAccess.database import Base
from datetime import datetime, timezone
from cuid import cuid

class Post(Base):
    __tablename__ = 'posts'

    id = Column(String, primary_key=True, default=lambda: cuid())
    content = Column(String)
    date = Column(DateTime, default=datetime.now(timezone.utc))