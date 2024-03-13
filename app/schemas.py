from pydantic import BaseModel


class CustomerBase(BaseModel):
    email: str
    name: str
    city: str


class CustomerUpdate(BaseModel):
    email: str | None
    name: str | None
    city: str | None


class CustomerCreate(CustomerBase):
    password: str


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
