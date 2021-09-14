import pytest
from starlette.testclient import TestClient

from webapi.app import app
from webapi.utils import security


@pytest.fixture(scope="module")
def test_app():
    client = TestClient(app)
    yield client


@pytest.fixture(scope='module')
def test_app_token():
    client = TestClient(app)
    token = "bearer " + security.create_access_token(1)
    client.headers = {
        'Authorization': token
    }
    yield client
