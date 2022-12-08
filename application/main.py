import logging

from repository.session import session
from requests.user import UserRequest
from use_cases.user import get_last_user_scraped
from use_cases.user import get_next_user
from use_cases.user import update_last_user
from use_cases.tweet import get_tweets_from_user
from use_cases.tweet import save_tweets_on_database


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def run() -> None:
    while True:
        # Get last user scraped, should return username
        last_user = get_last_user_scraped(session)
        # Get next user to be scrapped, should return username
        next_user = get_next_user(last_user, session)
        # Get user's tweets. Should return tweets or None
        tweets = get_tweets_from_user(next_user, session)

        if tweets:
            save_tweets_on_database(session)
            update_last_user(next_user, session)
            break

        update_last_user(next_user, session)


if __name__ == "__main__":
    run()
