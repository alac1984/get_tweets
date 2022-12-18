from unittest import mock

from use_cases.tweet import get_tweets_from_user
from use_cases.tweet import save_tweets_on_database
from repository.models.tweet import Tweet
from responses import Response
from requisitions import Requisition


def test_get_tweets_from_user_success(mock_tweets):
    req = Requisition(payload={"next_user_username": "pythonjazz"})
    with mock.patch("requests.get") as mocked_get:

        mocked_get.return_value = mock_tweets

        response = get_tweets_from_user(req)

    assert response is not None
    assert isinstance(response, Response)
    assert isinstance(response.content["data"], list)
    assert len(response.content["data"]) == 2


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


def test_save_tweets_on_database_new_tweets(mock_tweets, session):
    req = Requisition(payload=mock_tweets.json())

    response = save_tweets_on_database(req, session)

    tweets = session.query(Tweet).all()

    assert response is not None
    assert isinstance(response, Response)
    assert len(response.content) == 2
    assert tweets[0].id == 10293
    assert len(tweets) == 2


def test_save_tweets_on_database_one_inserted(mock_tweets, session):
    req = Requisition(payload=mock_tweets.json())
    response = save_tweets_on_database(req, session)

    inserted_tweet = {
        "data": [
            {
                "id": 10294,
                "user_id": 2,
                "created_at": "2022-12-14T02:51:10.000Z",
                "text": "É vóis",
                "lang": "en",
                "context_annotations": [
                    {"domain": {"id": 2, "name": "That", "description": "hell no"}}
                ],
            }
        ]
    }

    req = Requisition(payload=inserted_tweet)
    response = save_tweets_on_database(req, session)

    tweets = session.query(Tweet).all()

    assert response is not None
    assert isinstance(response, Response)
    assert len(response.content) == 0
    assert tweets[0].id == 10293
    assert len(tweets) == 2
