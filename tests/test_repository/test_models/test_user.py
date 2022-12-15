from datetime import datetime
from repository.models.user import User


def test_user_instantiation(session):
    user = User(
        twitter_id=939303,
        username="pythonjazz",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        description="A person",
        location="Fortaleza",
    )

    session.add(user)
    session.commit()

    assert user is not None
    assert user.id == 1
    assert user.twitter_id == 939303
