"""repository/user.py"""
import logging
from sqlalchemy.orm import Session

from entities.user import EntityUser
from .models.user import User

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def insert_user(user: EntityUser, session: Session):
    model_user = User(
        username=user.username,
        twitter_id=user.twitter_id,
        created_at=user.created_at,
        description=user.description,
        location=user.location,
    )
    logging.debug(f"model_user: {model_user}")
    session.add(model_user)
    session.commit()


def retrieve_last_scraped_user(session: Session):
    last_scraped_user = session.query(User).filter(User.last_scraped == True).first()

    return last_scraped_user


def retrieve_next_user_to_be_scraped(last_user_id: int, session: Session):
    next_user = session.query(User).filter(User.id == last_user_id + 1).first()
    if not next_user:
        next_user = session.query(User).filter(User.id == 1).first()

    return next_user


def update_last_scraped_user(prev_user_id: int, curr_user_id: int, session: Session):
    prev_user = session.query(User).filter(User.id == prev_user_id).first()
    curr_user = session.query(User).filter(User.id == curr_user_id).first()
    if prev_user and curr_user:
        prev_user.last_scraped = False
        curr_user.last_scraped = True
        session.add(prev_user)
        session.add(curr_user)
        session.commit()

        return True
    else:
        raise NotImplementedError
