from sqlalchemy.orm import Session

from repository.user import get_user
from requests import Request
from responses import Response


def get_last_user_scraped(request: Request, session: Session) -> Response:
    ...


def 
