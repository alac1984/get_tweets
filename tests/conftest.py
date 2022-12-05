import pytest
from repository import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@pytest.fixture(scope="function")
def engine():
    conn_str = "sqlite:///:memory:"
    engine = create_engine(conn_str, connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)


@pytest.fixture(scope="function")
def session(engine):
    connection = engine.connect()
    session = sessionmaker(autocommit=False, autoflush=False, bind=connection)
    session = session()

    yield session
    session.close()
    connection.close()
