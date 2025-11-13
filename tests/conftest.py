import pytest
from fastapi.testclient import TestClient

# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from main import app
from database import get_db, Base

from config import settings

# Create the new database session

SQLALCHEMY_DATABASE_URL = settings.postgresql_test_database_uri
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture()
def session():

    # Create the database

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client(session):

    # Dependency override

    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db

    yield TestClient(app)




'''from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings
import pytest
from database import Base
from pyodbc import ProgrammingErrorw
from typing import Generator
from sqlalchemy import text


# Set up a test database URL
TEST_SQLALCHEMY_DATABASE_URL: str = settings.POSTGRESQL_TEST_DATABASE_URI
admin_engine = create_engine(
   settings.POSTGRESQL_ADMIN_DATABASE_URI, isolation_level="AUTOCOMMIT"
)

# Create an engine and sessionmaker bound to the test database
engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_test_database():
    """Create the test database if it doesn't exist."""
    with admin_engine.connect() as connection:
        try:
            connection.execute(
                text(f"CREATE DATABASE {TEST_SQLALCHEMY_DATABASE_URL.split('/')[-1]}")
            )
        except ProgrammingError:
            print("Database already exists, continuing...")


@pytest.fixture(scope="session", autouse=True)
def setup_test_database():
    """
    Create the test database schema before any tests run,
    and drop it after all tests are done.
    """
    create_test_database()  # Ensure the test database is created
    Base.metadata.create_all(bind=engine)  # Create tables
    yield
    Base.metadata.drop_all(bind=engine)  # Drop tables after tests


@pytest.fixture(scope="function")
def db() -> Generator:
    """
    Create a new database session for each test and roll it back after the test.
    """
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()'''