from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from .database import get_db

app = FastAPI()


@app.get("/customers", response_model=List[int])
async def get_all_customers(db: Session = Depends(get_db)):
    customers = crud.get_customers(db=db)
    return [customer.id for customer in customers]


@app.get("/customers/{id}", response_model=schemas.Customer)
async def get_customer_by_id(id: int, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_id(db, customer_id=id)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer


@app.post("/create_customer", response_model=schemas.Customer, status_code=201)
async def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    db_customer = crud.get_customer_by_email(db, email=customer.email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_customer(db=db, email=customer.email, password=customer.password, name=customer.name, city=customer.city)


@app.put("/update_customer/{id}")
async def update_customer_by_id(customer: schemas.CustomerUpdate, id: int, db: Session = Depends(get_db)):
    db_customer = crud.update_customer_by_id(db, customer_id=id, data=customer)
    return db_customer


@app.get("/delete_customer/{id}")
async def delete_customer_by_id(id: int, db: Session = Depends(get_db)):
    return crud.delete_customer_by_id(db, id)
