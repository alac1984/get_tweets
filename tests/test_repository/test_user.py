"""tests/test_repository/test_user.py"""
import pytest
from datetime import datetime

from repository.models.user import User
from entities.user import EntityUser
from repository.user import insert_user
from repository.user import retrieve_last_scraped_user
from repository.user import retrieve_next_user


def test_insert_user(session):
    entity_user = EntityUser(
        username="anyone",
        created_at=datetime(2022, 1, 1, 1, 1, 1, 1),
        description="description",
        location="loc",
    )
    insert_user(entity_user, session)

    query_user = session.query(User).filter(User.id == 1).first()

    assert query_user.id == 1


def test_retrieve_last_scraped_user(init_db, session):
    last_user = retrieve_last_scraped_user(session)

    assert last_user is not None
    assert isinstance(last_user, User)
    assert last_user.id == 1


def test_retrieve_next_user(init_db, session):
    next_user = retrieve_next_user(1, session)

    assert next_user is not None
    assert isinstance(next_user, User)
    assert next_user.id == 2


def test_retrieve_next_user_error(init_db, session):
    next_user = retrieve_next_user(999999, session)

    assert next_user is not None
    assert isinstance(next_user, User)
    assert next_user.id == 1
