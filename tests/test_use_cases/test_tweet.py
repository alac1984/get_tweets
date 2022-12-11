from unittest import mock

from use_cases.tweet import get_tweets_from_user
from responses import Response
from requisitions import Requisition


def test_get_tweets_from_user_success(mock_tweets):
    req = Requisition(payload={"next_user_username": "pythonjazz"})
    with mock.patch("requests.get") as mocked_get:

        mocked_get.return_value = mock_tweets

        response = get_tweets_from_user(req)

    assert response is not None
    assert isinstance(response, Response)
    assert "tweets" in response.content
    assert isinstance(response.content["tweets"], list)


def test_get_tweets_from_user_no_tweets(mock_tweets):
    req = Requisition(payload={"next_user_username": "pythonjazz"})
    with mock.patch("requests.get") as mocked_get:
        mock_tweets._content = b""

        mocked_get.return_value = mock_tweets

        response = get_tweets_from_user(req)

    assert response is not None
    assert isinstance(response, Response)
    assert response.has_error()
    assert "JSONDecodeError" in response.errors[0]["name"]
