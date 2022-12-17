import logging

from repository.session import session
from requisitions import Requisition
from use_cases.user import get_id_last_user_scraped
from use_cases.user import get_next_user_to_be_scraped
from use_cases.user import change_last_user_scraped
from use_cases.user import flush_users
from use_cases.tweet import get_tweets_from_user
from use_cases.tweet import save_tweets_on_database


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


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


def run() -> bool:
    while True:
        req = Requisition()
        # Get id of last user scraped
        last_user_id = get_id_last_user_scraped(req, session).content[0][
            "last_user_id"
        ]

        # Get id of next user to be scrapped
        req = Requisition(payload={"last_user_id": last_user_id})
        next_user = get_next_user_to_be_scraped(req, session).content[0]

        # Get user's tweets
        req = Requisition(payload={"next_user_username": next_user["username"]})
        tweets = get_tweets_from_user(req).content

        req = Requisition(
            payload={
                "prev_user_id": last_user_id,
                "curr_user_id": next_user["id"],
            }
        )

        if len(tweets) > 0:
            save_tweets_on_database(req, session)
            change_last_user_scraped(req, session)
            return True

        change_last_user_scraped(req, session)


if __name__ == "__main__":
    run()
