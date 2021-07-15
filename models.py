from sqlalchemy import Column, String, Integer

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)

    city = Column(String, nullable=True)
    street = Column(String, nullable=True)
    house = Column(Integer, nullable=True)
