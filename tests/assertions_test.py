from core.libs import assertions
from core.libs.exceptions import FyleError

def test_base_assert():
    try:
        assertions.base_assert(500, "Internal Server Error")
    except FyleError as e:
        assert e.status_code == 500
        assert e.message == "Internal Server Error"
    else:
        assert False, "FyleError not raised"


def test_assert_auth():
    try:
        assertions.assert_auth(True)
    except FyleError:
        assert False, "FyleError raised unexpectedly"

    try:
        assertions.assert_auth(False)
    except FyleError as e:
        assert e.status_code == 401
        assert e.message == 'UNAUTHORIZED'
    else:
        assert False, "FyleError not raised"


def test_assert_true():
    try:
        assertions.assert_true(True)
    except FyleError:
        assert False, "FyleError raised unexpectedly"

    try:
        assertions.assert_true(False)
    except FyleError as e:
        assert e.status_code == 403
        assert e.message == 'FORBIDDEN'
    else:
        assert False, "FyleError not raised"


def test_assert_valid():
    try:
        assertions.assert_valid(True)
    except FyleError:
        assert False, "FyleError raised unexpectedly"

    try:
        assertions.assert_valid(False)
    except FyleError as e:
        assert e.status_code == 400
        assert e.message == 'BAD_REQUEST'
    else:
        assert False, "FyleError not raised"


def test_assert_found():
    try:
        assertions.assert_found("obj")
    except FyleError:
        assert False, "FyleError raised unexpectedly"

    try:
        assertions.assert_found(None)
    except FyleError as e:
        assert e.status_code == 404
        assert e.message == 'NOT_FOUND'
    else:
        assert False, "FyleError not raised"

