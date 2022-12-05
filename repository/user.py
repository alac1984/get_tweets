from sqlalchemy.orm import Session

from entities.user import EntityUser
from .models.user import User


def insert_user(user: EntityUser, session: Session):
    model_user = User(
        id=user.id,
        username=user.username,
        created_at=user.created_at,
        description=user.description,
        location=user.location,
    )
    session.add(model_user)
    session.commit()
