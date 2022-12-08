from requests import Request


def test_user_request_class():
    request = Request()

    assert request is not None


def test_build_user_request():
    request = Request()

    assert isinstance(request, Request)
