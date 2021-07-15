from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: str


class UserCreate(UserBase):
    id: str


class User(UserBase):
    id: str
    city: Optional[str]
    street: Optional[str]
    house: Optional[str]

    class Config:
        orm_mode = True
