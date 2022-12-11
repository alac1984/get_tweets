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


def save_tweet_on_database(user: str, tweet: dict) -> None:
    """
    Return False if tweet was not saved (was saved before)
    Return True otherwise
    """
    with psycopg2.connect(config.conn_str) as conn:
        cur = conn.cursor()
        cur.execute(
            """
             insert into tweets (id, username, text, detected) values
             (%s, %s, %s, %s)
        """,
            (tweet["id"], user, tweet["text"], datetime.now()),
        )
        conn.commit()


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
