from config import settings
import requests


def make_auth_header():
    token = settings.TWITTER_TOKEN
    return {"Authorization": f"Bearer {token}"}


def retrieve_tweets_from_user(user: str):
    auth_header = make_auth_header()
    response = requests.get(
        f"https://api.twitter.com/2/tweets/search/recent?query=from:{user}&tweet.fields=lang,author_id,context_annotations,created_at,entities",
        headers=auth_header,
    )
    return response.json() if response.content is not None else []
