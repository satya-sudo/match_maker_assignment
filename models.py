import uuid
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
        User table
        using uuid as the primary key 
        unique contraint on email.
        interests could have been a list or separate table.
        kept it as string for simplicity sake for now.
    """
    __tablename__ = 'users'

    id = Column(String, primary_key=True,
            default=lambda: str(uuid.uuid4()),
            unique=True,
            index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String, unique=True, index=True)
    city = Column(String)
    interests = Column(String)
