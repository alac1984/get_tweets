from sqlalchemy.orm import Session

from requests import Request
from responses import Response


def get_tweets_from_user(request: Request, user: str, session: Session) -> Response:
    ...


def save_tweets_on_database(
    request: Request, tweets: list[dict], session: Session
) -> Response:
    ...
