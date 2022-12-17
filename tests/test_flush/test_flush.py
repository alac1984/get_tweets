from unittest.mock import patch

from responses import Response
from application.user_creation import create_users


@patch("application.user_creation.flush_users")
def test_create_users(mock_flush):
    mock_flush.return_value = Response(content=[{"result": "yes"}])

    response = create_users()

    assert response is not None
    assert response.content == [{"result": "yes"}]
