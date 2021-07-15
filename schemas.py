from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: str


class UserCreate(UserBase):
    id: str
    city: Optional[str]
    street: Optional[str]
    house: Optional[int]


class User(UserBase):
    id: str
    city: Optional[str]
    street: Optional[str]
    house: Optional[int]

    class Config:
        orm_mode = True
