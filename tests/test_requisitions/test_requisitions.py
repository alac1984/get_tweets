from requisitions import Requisition


def test_user_request_class():
    req = Requisition()

    assert req is not None


def test_build_user_request():
    req = Requisition()

    assert isinstance(req, Requisition)
