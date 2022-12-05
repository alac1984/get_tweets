import pytest
from datetime import datetime
from sqlalchemy.sql import text

from repository.models.tweet import Tweet
from repository.models.tweet import Domain
from repository.models.tweet import Entity
from entities.tweet import EntityTweet
from entities.tweet import EntityDomain
from entities.tweet import EntityEntity
from repository.tweet import insert_tweet
from repository.tweet import insert_domain
from repository.tweet import insert_entity
from repository.tweet import insert_domain_tweet_relation
from repository.tweet import insert_entity_tweet_relation


@pytest.fixture
def init_db(engine):
    tweet = {
        "id": 1,
        "user_id": 1,
        "text": "This is a tweet",
        "lang": "pt-br",
        "created_at": datetime(2022, 1, 1, 1, 1, 1, 1),
    }
    user = {
        "id": 1,
        "username": "pythonjazz",
        "created_at": datetime(2022, 1, 1, 1, 1, 1, 1),
        "description": "The best",
        "location": "Fortaleza",
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
        conn.execute(ins_user_stmt, **user)
        conn.execute(ins_tweet_stmt, **tweet)


def test_insert_domain(session):
    entity_domain = EntityDomain(
        id=1,
        name="first_domain",
        description="description",
    )
    insert_domain(entity_domain, session)

    query_domain = session.query(Domain).filter(Domain.id == 1).first()

    assert query_domain.id == 1


def test_insert_domain_already_exist(session, init_db):
    ...


def test_insert_entity_already_exist(session, init_db):
    ...


def test_insert_entity(session):
    entity_entity = EntityEntity(
        id=1,
        name="first_entity",
        description="description",
    )
    insert_entity(entity_entity, session)

    query_entity = session.query(Entity).filter(Entity.id == 1).first()

    assert query_entity.id == 1


def test_insert_tweet_no_domain_no_entity(session, init_db):
    entity_tweet = EntityTweet(
        id=2,
        text="This is a tweet",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        user_id=1,
        lang="en",
    )
    insert_tweet(entity_tweet, session)

    query_tweet = session.query(Tweet).filter(Tweet.id == 2).first()

    assert query_tweet.id == 2


def test_insert_domain_tweet_relation(session):
    ...
