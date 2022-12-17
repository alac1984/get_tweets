from sqlalchemy.orm import Session

from repository.user import retrieve_last_scraped_user
from repository.user import retrieve_next_user_to_be_scraped
from repository.user import update_last_scraped_user
from repository.user import insert_user
from entities.user import EntityUser
from requisitions import Requisition
from responses import Response


def post_user(req: Requisition, session: Session) -> Response:
    response = Response()

    return response


def get_id_last_user_scraped(req: Requisition, session: Session) -> Response:
    response = Response()

    try:
        last_user = retrieve_last_scraped_user(session)
        response.content.append({"last_user_id": last_user.id})
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def get_next_user_to_be_scraped(req: Requisition, session: Session) -> Response:
    response = Response()

    try:
        last_user_id = req.payload["last_user_id"]
        next_user = retrieve_next_user_to_be_scraped(last_user_id, session)
        response.content.append({"id": next_user.id, "username": next_user.username})
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def change_last_user_scraped(req: Requisition, session: Session) -> Response:
    response = Response()
    prev_user_id = req.content[0]["prev_user_id"]
    curr_user_id = req.content[0]["curr_user_id"]

    try:
        result = update_last_scraped_user(prev_user_id, curr_user_id, session)
        response.content.append({"result": result})
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def flush_users(req: Requisition, session: Session) -> Response:
    response = Response()

    try:
        for user_data in req.payload:
            entity_user = EntityUser(**user_data)
            insert_user(entity_user, session)
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    response.content.append({"result": True})

    return response
