from datetime import datetime

from repository.models.user import User
from entities.user import EntityUser
from repository.user import insert_user


def test_insert_user(session):
    entity_user = EntityUser(
        id=29303,
        username="anyone",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        description="description",
        location="loc",
    )
    insert_user(entity_user, session)

    query_user = session.query(User).filter(User.id == 29303).first()

    assert query_user.id == 29303
