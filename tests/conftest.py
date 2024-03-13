import pytest
from sqlalchemy_utils import create_database, database_exists
from fastapi.testclient import TestClient
from homework_2.app.database import create_session, Base
from homework_2.app.models import Customers
from homework_2.app import app


class TestSettings:
    DATABASE_URL = "postgresql://user:password@localhost:5432/db-test"


@pytest.fixture(scope="session")
def db(session_mocker):
    session_mocker.patch("homework_2.app.database.get_settings", return_value=TestSettings())
    db_session = create_session()
    engine = db_session.bind
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.bind = engine
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    return db_session


@pytest.fixture()
def cleanup_db(db):
    for table in reversed(Base.metadata.sorted_tables):
        db.execute(table.delete())


@pytest.fixture()
def app_client(cleanup_db):
    yield TestClient(app=app.app)


@pytest.fixture()
def create_customer(db):
    customer = Customers(email="test@gmail.com", hashed_password="1234", city="test", name="test_wayne")
    db.add(customer)
    db.commit()
    yield customer
