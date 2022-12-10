"""entities/user.py"""
from pydantic import BaseModel
from datetime import datetime


class EntityUser(BaseModel):
    username: str
    created_at: datetime
    description: str
    location: str
