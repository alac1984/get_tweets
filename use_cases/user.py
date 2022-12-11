from sqlalchemy.orm import Session

from repository.user import retrieve_last_scraped_user
from repository.user import retrieve_next_user_to_be_scraped
from requisitions import Requisition
from responses import Response


def get_id_last_user_scraped(req: Requisition, session: Session) -> Response:
    response = Response()

    try:
        last_user = retrieve_last_scraped_user(session)
        response.content["last_user_id"] = last_user.id
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def get_next_user_to_be_scraped(req: Requisition, session: Session) -> Response:
    response = Response()

    try:
        last_user_id = req.payload["last_user_id"]
        next_user = retrieve_next_user_to_be_scraped(last_user_id, session)
        response.content["id"] = next_user.id
        response.content["username"] = next_user.username
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def update_last_user_scraped(
    req: Requisition, previous_scraped_id: int, last_scraped_id: int, session: Session
) -> Response:
    ...
