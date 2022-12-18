from unittest import mock

from external_apis.twitter import retrieve_tweets_from_user


def test_retrieve_tweets_from_user(mock_tweets):
    with mock.patch("requests.get") as mocked_get:
        mocked_get.return_value = mock_tweets

        tweets = retrieve_tweets_from_user("pythonjazz")

        assert tweets is not None
        assert tweets["data"][0]["id"] == 10293
