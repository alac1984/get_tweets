"""tests/test_use_cases/test_user.py"""
from requisitions import Requisition
from responses import Response
from use_cases.user import get_id_last_user_scraped
from use_cases.user import get_next_user_to_be_scraped


def test_get_id_last_user_scraped(init_db, session):
    req = Requisition()
    response = get_id_last_user_scraped(req, session)

    assert response.content is not None
    assert isinstance(response, Response)
    assert response.content["last_user_id"] == 1


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
    assert response.content["id"] == 2
