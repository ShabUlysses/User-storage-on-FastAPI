from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=False, index=True)
    email = Column(String(50), unique=True, index=True)
    city = Column(String(50), unique=False, index=True)
    hashed_password = Column(String(50))
