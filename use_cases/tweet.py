from sqlalchemy.orm import Session

from requests import Request
from responses import Response


def get_tweets_from_user(user: str, session: Session) -> Response:
    ...


def save_tweets_on_database(tweets: list[dict], session: Session) -> Response:
    ...
