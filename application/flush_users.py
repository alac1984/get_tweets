from requisitions import Requisition
from repository.session import session
from repository.user import flush_users


def create_users():
    users = [
        {
            "twitter_id": 1420152235145797632,
            "created_at": "",
            "username": "",
            "last_scraped": True,
        },
        {
            "twitter_id": 575522002,
            "created_at": "",
            "username": "",
        },
        {
            "twitter_id": 1603953685205336065,
            "created_at": "",
            "username": "",
        },
        {
            "twitter_id": 313074549,
            "created_at": "",
            "username": "",
        },
        {
            "twitter_id": 30541996,
            "created_at": "",
            "username": "",
        },
    ]

    req = Requisition(payload=users)

    flush_users(req, session)


if __name__ == "__main__":
    flush_users()
