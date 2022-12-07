from sqlalchemy.orm import Session

from entities.tweet import EntityTweet
from .models.tweet import Tweet
from .models.tweet import Domain
from .models.tweet import Entity


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
            model_entity = Entity(
                id=entity.id,
                name=entity.name,
                description=entity.description,
            )
            model_tweet.entities.append(model_entity)

    if tweet.domains:
        for domain in tweet.domains:
            model_domain = Domain(
                id=domain.id,
                name=domain.name,
                description=domain.description,
            )
            model_tweet.domains.append(model_domain)

    session.add(model_tweet)
    session.commit()
