from requests.tweet import build_tweet_request
from requests.tweet import TweetRequest


def test_tweet_request_class():
    request = TweetRequest()

    assert request is not None


def test_build_tweet_request():
    request = build_tweet_request()

    assert isinstance(request, TweetRequest)
