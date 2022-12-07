from requests.user import build_user_request
from requests.user import UserRequest


def test_user_request_class():
    request = UserRequest()

    assert request is not None


def test_build_user_request():
    request = build_user_request()

    assert isinstance(request, UserRequest)
