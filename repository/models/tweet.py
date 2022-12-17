from __future__ import annotations

from sqlalchemy import (
    Table,
    Column,
    Integer,
    BigInteger,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, relationship, backref

from repository.base import Base


tb_tweet_domain = Table(
    "tb_tweet_domain",
    Base.metadata,
    Column("tweet_id", ForeignKey("tb_tweet.id"), primary_key=True),
    Column("domain_id", ForeignKey("tb_domain.id"), primary_key=True),
)


tb_tweet_entity = Table(
    "tb_tweet_entity",
    Base.metadata,
    Column("tweet_id", ForeignKey("tb_tweet.id"), primary_key=True),
    Column("entity_id", ForeignKey("tb_entity.id"), primary_key=True),
)


class Tweet(Base):
    __tablename__ = "tb_tweet"

    id = Column(BigInteger(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("tb_user.id"))
    created_at = Column(DateTime(), nullable=False)
    lang = Column(String(), nullable=False)
    text = Column(String(), nullable=False)

    domains: Mapped[list[Domain]] = relationship(
        "Domain", secondary=tb_tweet_domain, back_populates="tweets"
    )
    entities: Mapped[list[Entity]] = relationship(
        "Entity", secondary=tb_tweet_entity, back_populates="tweets"
    )

    user = relationship("User", backref=backref("tweets", order_by=created_at))  # type: ignore


class Domain(Base):
    __tablename__ = "tb_domain"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)

    tweets: Mapped[list[Tweet]] = relationship(
        "Tweet", secondary=tb_tweet_domain, back_populates="domains"
    )


class Entity(Base):
    __tablename__ = "tb_entity"

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)

    tweets: Mapped[list[Tweet]] = relationship(
        "Tweet", secondary=tb_tweet_entity, back_populates="entities"
    )
