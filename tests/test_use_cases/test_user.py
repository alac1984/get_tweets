"""tests/test_use_cases/test_user.py"""
from requisitions import Requisition
from responses import Response
from use_cases.user import get_id_last_user_scraped
from use_cases.user import get_next_user_to_be_scraped
from use_cases.user import flush_users


def test_get_id_last_user_scraped_success(init_db, session):
    req = Requisition()
    response = get_id_last_user_scraped(req, session)

    assert response.content is not None
    assert isinstance(response, Response)
    assert response.content[0]["last_user_id"] == 1


def test_get_id_last_user_scraped_without_data(session):
    req = Requisition()
    response = get_id_last_user_scraped(req, session)

    assert bool(response) is False
    assert response.has_error() is True
    assert isinstance(response.errors[0], dict)
    assert "AttributeError" in response.errors[0]["name"]


def test_get_next_user_to_be_scraped(init_db, session):
    req = Requisition(payload={"last_user_id": 1})
    response = get_next_user_to_be_scraped(req, session)

    assert response is not None
    assert bool(response) is True
    assert response.has_error() is False
    assert isinstance(response, Response)
    assert response.content[0]["id"] == 2


def test_flush_users(session):
    req = Requisition(
        payload=[
            {
                "twitter_id": 1029,
                "created_at": "2010-07-03T18:26:22.000Z",
                "username": "this",
            },
            {
                "twitter_id": 1030,
                "created_at": "2010-07-03T18:26:22.000Z",
                "username": "that",
            },
            {
                "twitter_id": 1031,
                "created_at": "2010-07-03T18:26:22.000Z",
                "username": "those",
            },
        ]
    )
    response = flush_users(req, session)

    assert response is not None
    assert response.content[0]["result"] is True


def test_flush_user(session):
    users = [
        {
            "twitter_id": 1420152235145797632,
            "created_at": "2021-07-27T22:41:05.000Z",
            "username": "pythonjazz",
            "last_scraped": True,
        },
        {
            "twitter_id": 575522002,
            "created_at": "2012-05-09T17:06:03.000Z",
            "username": "Bruna_Hawk",
        },
    ]

    req = Requisition(payload=users)

    response = flush_users(req, session)

    assert response is not None
