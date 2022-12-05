from datetime import datetime

from pydantic import BaseModel


class EntityDomain(BaseModel):
    id: int
    name: str
    description: str


class EntityEntity(BaseModel):  # I swear it's not a joke
    id: int
    name: str
    description: str


class EntityTweet(BaseModel):
    id: int
    user_id: int
    text: str
    created_at: datetime
    lang: str
    domains: list[EntityDomain] = None
    entities: list[EntityEntity] = None
