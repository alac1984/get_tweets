import logging

from repository.session import session
from requisitions import Requisition
from use_cases.user import get_id_last_user_scraped
from use_cases.user import get_next_user_to_be_scraped
from use_cases.user import change_last_user_scraped
from use_cases.tweet import get_tweets_from_user
from use_cases.tweet import save_tweets_on_database


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


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

        req_change = Requisition(
            payload={
                "prev_user_id": last_user_id,
                "curr_user_id": next_user["id"],
            }
        )

        req_save = Requisition(payload=tweets)

        if len(tweets) > 0:
            save_tweets_on_database(req_save, session)
            change_last_user_scraped(req_change, session)
            return True

        change_last_user_scraped(req, session)


if __name__ == "__main__":
    run()
