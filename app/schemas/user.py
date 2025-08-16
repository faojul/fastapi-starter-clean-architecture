from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import Role

class UserBase(BaseModel):
    email: EmailStr
    role: Role = Role.USER

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    role: Optional[Role] = None

class UserInDB(UserBase):
    id: int

    class Config:
        model_config = {"from_attributes": True}