from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings


def get_engine():
    engine = create_engine(str(get_settings().DATABASE_URL))
    return engine


def create_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=get_engine())
    return SessionLocal()


def get_db():
    try:
        db = create_session()
        yield db
    finally:
        db.close()


Base = declarative_base()
