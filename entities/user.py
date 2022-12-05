from pydantic import BaseModel
from datetime import datetime


class EntityUser(BaseModel):
    id: int
    username: str
    created_at: datetime
    description: str
    location: str
