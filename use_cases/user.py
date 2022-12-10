from sqlalchemy.orm import Session

from repository.user import retrieve_last_scraped_user
from repository.user import retrieve_next_user
from requests import Request
from responses import Response


def get_last_user_scraped(request: Request, session: Session) -> Response:
    response = Response()
    try:
        last_user = retrieve_last_scraped_user(session)
        response.content["last_user_id"] = last_user.id
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def get_next_user(request: Request, last_user_id: int, session: Session) -> Response:
    response = Response()
    try:
        next_user = retrieve_next_user(last_user_id, session)
        response.content["next_user_id"] = next_user.id
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def update_last_user(request: Request, user: str, session: Session) -> Response:
    ...
