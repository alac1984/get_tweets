import pytest
from datetime import datetime
from sqlalchemy.exc import IntegrityError
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
    with pytest.raises(IntegrityError):
        entity_domain = EntityDomain(
            id=1,
            name="first_domain",
            description="description",
        )
        insert_domain(entity_domain, session)


def test_insert_entity_already_exist(session, init_db):
    with pytest.raises(IntegrityError):
        entity_entity = EntityEntity(
            id=1,
            name="first_entity",
            description="description",
        )
        insert_entity(entity_entity, session)


def test_insert_entity(session):
    entity_entity = EntityEntity(
        id=1,
        name="first_entity",
        description="description",
    )
    insert_entity(entity_entity, session)

    query_entity = session.query(Entity).filter(Entity.id == 1).first()

    assert query_entity.id == 1


def test_insert_tweet_no_domain_no_entity(session):
    entity_tweet = EntityTweet(
        id=1,
        text="This is a tweet",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        user_id=1,
        lang="en",
    )
    insert_tweet(entity_tweet, session)

    query_tweet = session.query(Tweet).filter(Tweet.id == 1).first()

    assert query_tweet.id == 1


def test_insert_tweet_with_domain_and_entity(full_tweet, session):
    entity_domain = EntityDomain(
        id=1,
        name="first_domain",
        description="description",
    )
    entity_entity = EntityEntity(
        id=1,
        name="first_entity",
        description="description",
    )
    entity_tweet = EntityTweet(
        id=1,
        text="This is a tweet",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        user_id=1,
        lang="en",
        domains=[entity_domain],
        entities=[entity_entity],
    )
    insert_tweet(entity_tweet, session)

    query_tweet = session.query(Tweet).filter(Tweet.id == 1).first()

    assert query_tweet.id == 1


def test_insert_domain_tweet_relation(session, engine, init_db):
    insert_domain_tweet_relation(1, 2, session)

    with engine.connect() as conn:
        sel_stmt = text("select * from tb_tweet_domain where tweet_id = :tweet_id")
        result = conn.execute(sel_stmt, {"tweet_id": 2}).fetchone()

    assert result == (2, 1)


def test_insert_entity_tweet_relation(session, engine, init_db):
    insert_entity_tweet_relation(1, 2, session)

    with engine.connect() as conn:
        sel_stmt = text("select * from tb_tweet_entity where tweet_id = :tweet_id")
        result = conn.execute(sel_stmt, {"tweet_id": 2}).fetchone()

    assert result == (2, 1)
