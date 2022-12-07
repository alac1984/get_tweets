from requests.base import BaseRequest


class TweetRequest(BaseRequest):
    ...


def build_tweet_request():
    request = TweetRequest()
    return request
