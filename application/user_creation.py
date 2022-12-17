import logging
from requisitions import Requisition
from repository.session import session
from use_cases.user import flush_users

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def create_users():
    users = [
        {
            "twitter_id": 1420152235145797632,
            "created_at": "2021-07-27T22:41:05.000Z",
            "username": "pythonjazz",
            "last_scraped": True,
        },
        {
            "twitter_id": 575522002,
            "created_at": "2012-05-09T17:06:03.000Z",
            "username": "Bruna_Hawk",
        },
        {
            "twitter_id": 896171046,
            "created_at": "2012-10-21T21:15:00.000Z",
            "username": "rebecamaia_p",
        },
        {
            "twitter_id": 313074549,
            "created_at": "2011-06-08T03:21:19.000Z",
            "username": "dorafigueiredo",
        },
        {
            "twitter_id": 30541996,
            "created_at": "2009-04-11T22:38:58.000Z",
            "username": "dai_tama",
        },
    ]

    req = Requisition(payload=users)

    response = flush_users(req, session)

    return response


if __name__ == "__main__":
    logging.debug("Flushing users...")
    response = create_users()
    logging.debug(f"{response.content}")
