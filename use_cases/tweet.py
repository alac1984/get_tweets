from sqlalchemy.orm import Session

from requisitions import Requisition
from responses import Response
from external_apis.twitter import retrieve_tweets_from_user
from repository.tweet import insert_tweet
from entities.tweet import EntityTweet


def get_tweets_from_user(req: Requisition):
    response = Response()
    try:
        tweets = retrieve_tweets_from_user(req.payload["next_user_username"])
        response.content = tweets
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def save_tweets_on_database(req: Requisition, session: Session) -> Response:
    response = Response()
    for tweet in req.payload:
        try:
            entity_tweet = EntityTweet(**tweet)
            insert_tweet(entity_tweet, session)
            response.content.append({entity_tweet.id: entity_tweet.text})
        except Exception as e:
            response.add_error(str(e.__class__), e.__str__())

    return response
