from sqlalchemy.orm import Session

from repository.user import retrieve_last_scraped_user
from requests import Request
from responses import Response


def get_last_user_scraped(request: Request, session: Session) -> Response:
    response = Response()
    try:
        user = retrieve_last_scraped_user(session)
        response.content["username"] = user.username
    except Exception as e:
        response.add_error(str(e.__class__), e._message)

    return response


def get_next_user(request: Request, last_user: str, session: Session) -> Response:
    ...


def update_last_user(user: str, session: Session) -> Response:
    ...
