"""repository/user.py"""
from sqlalchemy.orm import Session

from entities.user import EntityUser
from .models.user import User


def insert_user(user: EntityUser, session: Session):
    model_user = User(
        username=user.username,
        created_at=user.created_at,
        description=user.description,
        location=user.location,
    )
    session.add(model_user)
    session.commit()


def retrieve_last_scraped_user(session: Session):
    last_scraped_user = session.query(User).filter(User.last_scraped == True).first()

    return last_scraped_user


def retrieve_next_user(last_user_id: int, session: Session):
    next_user = session.query(User).filter(User.id == last_user_id + 1).first()
    if not next_user:
        next_user = session.query(User).filter(User.id == 1).first()

    return next_user
