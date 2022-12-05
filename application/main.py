import logging

# from twitter import get_tweets_from_user
# from twitter import save_tweet_on_database
# from twitter import tweet_was_saved_before
# from users import get_next_user
# from users import get_last_user

from repository.models.tweet import Domain
from repository.session import session

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def run() -> None:
    domain = Domain(id=123, name="test_domain", description="description test")
    session.add(domain)
    session.commit()


# def run() -> None:
#     last_user = get_last_user()
#     user = get_next_user(last_user)
#     logging.debug(f"user selected is {user}")
#     tweets = get_tweets_from_user(user)

#     if tweets.get('title', None) == "Too Many Requests":
#         logging.debug("too many requests for Twitter API")
#         return

#     if tweets.get('meta', None):
#         while tweets['meta']['result_count'] == 0:
#             logging.debug(f"user {user} has no recent tweets")
#             user = get_next_user(user)
#             logging.debug(f"new user is {user}")
#             tweets = get_tweets_from_user(user)

#     count = 0
#     for tweet in tweets["data"]:
#         if tweet_was_saved_before(tweet['id']):
#             continue

#         save_tweet_on_database(user, tweet)
#         count += 1

#     logging.debug(f"{count} tweets from user {user} saved in database")

if __name__ == "__main__":
    run()
