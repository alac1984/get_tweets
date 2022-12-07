from requests.base import BaseRequest


class UserRequest(BaseRequest):
    ...


def build_user_request():
    request = UserRequest()
    return request
