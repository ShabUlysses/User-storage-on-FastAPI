from sqlalchemy.orm import Session

from . import models, schemas


def get_customer_by_id(db: Session, customer_id: int):
    return db.query(models.Customers).filter(models.Customers.id == customer_id).first()


def delete_customer_by_id(db: Session, customer_id: int):
    db.query(models.Customers).filter(models.Customers.id == customer_id).delete()
    db.commit()
    return 'Customer deleted'


def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customers).filter(models.Customers.email == email).first()


def update_customer_by_id(db: Session, customer_id: int, data):
    db_customer = db.query(models.Customers).filter(models.Customers.id == customer_id).first()
    if data.name:
        setattr(db_customer, "name", data.name)
    if data.email:
        setattr(db_customer, "email", data.email)
    if data.city:
        setattr(db_customer, "city", data.city)
    db.commit()
    return db_customer



def create_customer(db: Session, email: str, password: str, name: str, city: str):
    hashed_password = password + "hash"
    db_customer = models.Customers(email=email, hashed_password=hashed_password, name=name, city=city)
    db.add(db_customer)
    db.commit()
    return db_customer


def get_customers(db: Session):
    return db.query(models.Customers).order_by(models.Customers.id.asc()).all()
