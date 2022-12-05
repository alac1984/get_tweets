from sqlalchemy import insert
from sqlalchemy.orm import Session

from entities.tweet import EntityTweet
from entities.tweet import EntityDomain
from entities.tweet import EntityEntity
from .models.tweet import Tweet
from .models.tweet import Domain
from .models.tweet import Entity
from .models.tweet import tb_tweet_domain
from .models.tweet import tb_tweet_entity


def insert_domain(domain: EntityDomain, session: Session):
    has_domain = session.query(Domain).filter(Domain.id == domain.id).first()
    if not has_domain:
        model_domain = Domain(
            id=domain.id, name=domain.name, description=domain.description
        )
        session.add(model_domain)
        session.commit()


def insert_entity(entity: EntityEntity, session: Session):
    has_entity = session.query(Entity).filter(Entity.id == entity.id).first()
    if not has_entity:
        model_entity = Entity(
            id=entity.id, name=entity.name, description=entity.description
        )
        session.add(model_entity)
        session.commit()


def insert_domain_tweet_relation(domain_id: int, tweet_id: int, session: Session):
    ins = insert(tb_tweet_domain).values(
        tweet_id=tweet_id,
        domain_id=domain_id,
    )
    session.execute(ins)
    session.commit()


def insert_entity_tweet_relation(entity_id: int, tweet_id: int, session: Session):
    ins = insert(tb_tweet_entity).values(
        tweet_id=tweet_id,
        entity_id=entity_id,
    )
    session.execute(ins)
    session.commit()


def insert_tweet(tweet: EntityTweet, session: Session):
    model_tweet = Tweet(
        id=tweet.id,
        user_id=tweet.user_id,
        created_at=tweet.created_at,
        text=tweet.text,
        lang=tweet.lang,
    )

    if tweet.entities:
        for entity in tweet.entities:
            insert_entity(entity, session)
            insert_entity_tweet_relation(tweet.id, entity.id, session)

    if tweet.domains:
        for domain in tweet.domains:
            insert_domain(domain, session)
            insert_domain_tweet_relation(tweet.id, domain.id, session)

    session.add(model_tweet)
    session.commit()
