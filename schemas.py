from pydantic import BaseModel, EmailStr
from typing import Optional

# Base schema for the User model
class UserBase(BaseModel):
    name: str
    age: int
    gender: str
    email: EmailStr
    city: str
    interests: str

# Schema for creating a new user
class UserCreate(UserBase):
    pass

# Schema for updating an existing user
class UserUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    interests: Optional[str] = None

# Schema for response data
class UserResponse(UserBase):
    id: str

    class Config:
        from_attributes = True 

class UserMatch(BaseModel):
    id: str
    name: str
    city: str
    interests: str

    class Config:
        from_attributes = True
