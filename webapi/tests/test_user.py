from starlette.testclient import TestClient

from webapi.setting import settings


def test_login(test_app: TestClient):
    form_data = {
        'username': settings.ADMIN_USERNAME,
        'password': settings.ADMIN_PASSWORD
    }
    response = test_app.post(url='/api/admin/login/access_token/', data=form_data)
    assert response.status_code == 201
    json_data = response.json()
    assert 'access_token' in json_data
    assert 'token_type' in json_data


def test_error_login(test_app: TestClient):
    form_data = {
        'username': settings.ADMIN_USERNAME,
        'password': 'xansjwq'
    }
    response = test_app.post(url='/api/admin/login/access_token/', data=form_data)
    assert response.status_code == 400


def test_login_getinfo(test_app: TestClient):
    form_data = {
        'username': settings.ADMIN_USERNAME,
        'password': settings.ADMIN_PASSWORD
    }
    response = test_app.post(url='/api/admin/login/access_token/', data=form_data)
    assert response.status_code == 201
    json_data = response.json()
    token = json_data['token_type'] + ' ' + json_data['access_token']

    headers = {
        'Authorization': token
    }
    response = test_app.get(url='/api/admin/login/getinfo', headers=headers)
    assert response.status_code == 200


def test_login_getinfo_error(test_app: TestClient):
    response = test_app.get(url='/api/admin/login/getinfo')
    assert response.status_code == 401
