from datetime import datetime
from config import config
import requests


def make_auth_header():
    token = config.TWITTER_TOKEN
    return {"Authorization": f"Bearer {token}"}


def retrieve_tweets_from_user(user: str):
    auth_header = make_auth_header()
    response = requests.get(
        f"https://api.twitter.com/2/tweets/search/recent?query=from:{user}",
        headers=auth_header,
    )
    return response.json() if response.content is not None else []


def tweet_was_saved_before(tweet_id: int) -> bool:
    """
    Return True if tweet was saved before
    Return False otherwise
    """
    with psycopg2.connect(config.conn_str) as conn:
        cur = conn.cursor()
        cur.execute("select id from tweets where id = %s", (tweet_id,))
        result = cur.fetchall()
        return False if len(result) == 0 else True
