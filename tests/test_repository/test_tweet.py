"""tests/test_repository/test_tweet.py"""
import pytest
from datetime import datetime

from repository.models.tweet import Tweet
from entities.tweet import EntityTweet
from entities.tweet import EntityDomain
from entities.tweet import EntityEntity
from repository.tweet import insert_tweet


@pytest.fixture
def full_tweet():
    entity_domain1 = EntityDomain(
        id=1,
        name="first_domain",
        description="description",
    )
    entity_domain2 = EntityDomain(
        id=2,
        name="first_domain",
        description="description",
    )
    entity_entity1 = EntityEntity(
        id=1,
        name="first_entity",
        description="description",
    )
    entity_entity2 = EntityEntity(
        id=2,
        name="first_entity",
        description="description",
    )
    entity_tweet = EntityTweet(
        id=1,
        text="This is a tweet",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        user_id=1,
        lang="en",
        domains=[entity_domain1, entity_domain2],
        entities=[entity_entity1, entity_entity2],
    )

    return entity_tweet


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
    insert_tweet(full_tweet, session)

    query_tweet = session.query(Tweet).filter(Tweet.id == 1).first()

    assert query_tweet.id == 1
    assert len(query_tweet.domains) == 2
    assert len(query_tweet.entities) == 2
