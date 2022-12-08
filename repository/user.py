from sqlalchemy import desc
from sqlalchemy.orm import Session

from entities.user import EntityUser
from .models.user import User
from .models.user import ScrapedUser


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


def retrieve_last_scraped_user(session: Session):
    scraped_user = (
        session.query(ScrapedUser)
        .order_by(desc(ScrapedUser.scraped_on))
        .limit(1)
        .one()
    )

    model_user = session.query(User).filter(User.id == scraped_user.user_id).first()

    return model_user
