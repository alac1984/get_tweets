"""tests/test_use_cases/test_user.py"""
from requests import Request
from responses import Response
from use_cases.user import get_last_user_scraped


def test_get_last_user_scraped(init_db, session):
    request = Request()
    response = get_last_user_scraped(request, session)

    assert isinstance(response, Response)
    assert response.content is not None
    assert response.content["last_user_id"] == 1


def test_get_last_user_scraped_without_data(session):
    request = Request()
    response = get_last_user_scraped(request, session)

    assert bool(response) is False
    assert response.has_error() is True
    assert isinstance(response.errors[0], dict)
    assert "AttributeError" in response.errors[0]["name"]
