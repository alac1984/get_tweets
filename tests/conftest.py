import pytest
from datetime import datetime
from sqlalchemy.sql import text

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


@pytest.fixture
def init_db(engine):
    tweet1 = {
        "id": 1,
        "user_id": 1,
        "text": "This is a tweet",
        "lang": "pt-br",
        "created_at": datetime(2022, 1, 1, 1, 1, 1, 1),
    }
    tweet2 = {
        "id": 2,
        "user_id": 1,
        "text": "This is a new tweet",
        "lang": "en",
        "created_at": datetime(2022, 1, 1, 1, 1, 1, 1),
    }
    user = {
        "id": 1,
        "username": "pythonjazz",
        "created_at": datetime(2022, 1, 1, 1, 1, 1, 1),
        "description": "The best",
        "location": "Fortaleza",
    }
    scraped_user = {
        "id": 1,
        "user_id": 1,
        "scraped_on": datetime(2022, 1, 1, 1, 1, 1, 1),
    }
    domain = {
        "id": 1,
        "name": "Domain 1",
        "description": "The best domain",
    }
    entity = {
        "id": 1,
        "name": "Entity 1",
        "description": "The best entity",
    }
    with engine.connect() as conn:
        ins_user_stmt = text(
            """
            insert into tb_user(id, username, created_at, description, location)
            values(:id, :username, :created_at, :description, :location);
            """
        )
        ins_tweet_stmt = text(
            """
            insert into tb_tweet(id, user_id, text, lang, created_at)
            values(:id, :user_id, :text, :lang, :created_at);
            """
        )
        ins_scraped_user_stmt = text(
            """
            insert into tb_scraped_user(id, user_id, scraped_on)
            values(:id, :user_id, :scraped_on);
            """
        )
        ins_domain_stmt = text(
            """
            insert into tb_domain(id, name, description)
            values(:id, :name, :description);
            """
        )
        ins_entity_stmt = text(
            """
            insert into tb_entity(id, name, description)
            values(:id, :name, :description);
            """
        )
        ins_domain_tweet_stmt = text(
            """
            insert into tb_tweet_domain(tweet_id, domain_id)
            values(:tweet_id, :domain_id);
            """
        )
        ins_entity_tweet_stmt = text(
            """
            insert into tb_tweet_entity(tweet_id, entity_id)
            values(:tweet_id, :entity_id);
            """
        )
        conn.execute(ins_user_stmt, **user)
        conn.execute(ins_scraped_user_stmt, **scraped_user)
        conn.execute(ins_tweet_stmt, **tweet1)
        conn.execute(ins_tweet_stmt, **tweet2)
        conn.execute(ins_domain_stmt, **domain)
        conn.execute(ins_entity_stmt, **entity)
        conn.execute(
            ins_domain_tweet_stmt,
            **{
                "tweet_id": 1,
                "domain_id": 1,
            },
        )
        conn.execute(
            ins_entity_tweet_stmt,
            **{
                "tweet_id": 1,
                "entity_id": 1,
            },
        )
