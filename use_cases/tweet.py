from external_apis.twitter import retrieve_tweets_from_user
from requisitions import Requisition
from responses import Response


def get_tweets_from_user(req: Requisition):
    response = Response()
    try:
        tweets = retrieve_tweets_from_user(req.payload["next_user_username"])
        response.content["tweets"] = tweets
    except Exception as e:
        response.add_error(str(e.__class__), e.__str__())

    return response


def save_tweets_on_database(req: Requisition, tweets: list[dict]) -> Response:
    response = Response()

    return response
