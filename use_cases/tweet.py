import logging
from sqlalchemy.orm import Session

from requisitions import Requisition
from responses import Response
from external_apis.twitter import retrieve_tweets_from_user
from repository.tweet import insert_tweet
from repository.tweet import get_list_tweet_ids
from entities.tweet import EntityTweet
from .utils import check_if_tweet_was_saved_before


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def get_tweets_from_user(req: Requisition):
    response = Response()
    try:
        tweets = retrieve_tweets_from_user(req.payload["next_user_username"])
        response.content = tweets
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    logging.debug(f"retrieve tweets: {response}")
    return response


def save_tweets_on_database(req: Requisition, session: Session) -> Response:
    response = Response()
    ids = get_list_tweet_ids(session)
    for tweet in req.payload["data"]:
        if check_if_tweet_was_saved_before(tweet["id"], ids):
            continue

        try:
            entity_tweet = EntityTweet(**tweet)
            insert_tweet(entity_tweet, session)
            response.content.append({entity_tweet.id: entity_tweet.text})
        except Exception as e:
            response.add_error(str(e.__class__), e.__str__())

    logging.debug(f"save tweets: {response}")
    return response
