from unittest.mock import patch
from unittest.mock import MagicMock

from responses import Response
from application.main import run


@patch("application.main.get_id_last_user_scraped")
@patch("application.main.get_next_user_to_be_scraped")
@patch("application.main.get_tweets_from_user")
@patch("application.main.save_tweets_on_database")
@patch("application.main.change_last_user_scraped")
def test_run(
    mock_change_last, mock_save_tweets, mock_get_tweets, mock_get_next, mock_get_id
):
    mock_get_id.return_value = Response(content=[{"last_user_id": 1}])
    mock_get_next.return_value = Response(content=[{"id": 1, "username": "testuser"}])
    mock_get_tweets.return_value = Response(
        content=[
            {
                "id": 10293,
                "user_id": 1,
                "created_at": "2022-12-14T02:51:10.000Z",
                "text": "É tóis",
                "lang": "pt",
                "context_annotations": [
                    {"domain": {"id": 1, "name": "This", "description": "hell yeah"}}
                ],
            },
            {
                "id": 10294,
                "user_id": 2,
                "created_at": "2022-12-14T02:51:10.000Z",
                "text": "É vóis",
                "lang": "en",
                "context_annotations": [
                    {"domain": {"id": 2, "name": "That", "description": "hell no"}}
                ],
            },
        ]
    )
    mock_save_tweets.return_value = Response(
        content=[
            {"id": 10293, "text": "É tóis"},
            {"id": 10294, "text": "É vóis"},
        ]
    )
    mock_change_last.return_value = Response(content=[{"result": True}])
    result = run()

    assert result is True
