import json
import pytest
from starlette.testclient import TestClient
from webapi.db.dals.category_dal import Category, CategoryDAL


def test_create_category_no_token(test_app: TestClient, monkeypatch):
    data = {
        'name': 'Category1'
    }
    response = test_app.post(url='/api/categories/', json=data)
    assert response.status_code == 401


def test_create_category(test_app_token: TestClient, monkeypatch):
    data = {
        'name': 'Category1'
    }
    response_data = {
        'name': 'Category1',
        'id': 1
    }

    async def mock_get_by_name(self, name):
        return None

    async def mock_create(self, b):
        return Category(**response_data)

    monkeypatch.setattr(CategoryDAL, "create", mock_create)
    monkeypatch.setattr(CategoryDAL, "get_by_name", mock_get_by_name)
    response = test_app_token.post(url='/api/categories/', json=data)
    assert response.status_code == 201
    assert response.json() == response_data


def test_create_category_exists(test_app_token: TestClient, monkeypatch):
    data = {
        'name': 'Category1'
    }

    response_data = {
        'name': 'Category1',
        'id': 1
    }

    async def mock_get_by_name(self, name):
        return 'Category1'

    async def mock_create(self, b):
        return Category(**response_data)

    monkeypatch.setattr(CategoryDAL, "create", mock_create)
    monkeypatch.setattr(CategoryDAL, "get_by_name", mock_get_by_name)
    response = test_app_token.post(url='/api/categories/', json=data)
    assert response.status_code == 400


def test_create_category_invalid_data(test_app_token: TestClient):
    response = test_app_token.post(url='/api/categories/', json={})
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "name"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_all_categories(test_app: TestClient, monkeypatch):
    test_data = [
        {
            "id": 1,
            "name": "Category1",
            "posts": 10
        },
        {
            "id": 2,
            "name": "Category2",
            "posts": 20
        }
    ]

    test_total = 2

    test_result = {
        'total': test_total,
        'items': test_data
    }

    async def mock_count(self, name=None):
        return test_total

    async def mock_get_all(self, name=None):
        return test_data

    monkeypatch.setattr(CategoryDAL, "count", mock_count)
    monkeypatch.setattr(CategoryDAL, "get_all", mock_get_all)

    response = test_app.get(url='/api/categories/')
    assert response.status_code == 200
    assert response.json() == test_result


def test_read_categories_selection(test_app: TestClient, monkeypatch):
    test_data = [
        {
            "id": 1,
            "name": "Category1"
        },
        {
            "id": 2,
            "name": "Category2"
        }
    ]

    async def mock_get_selection(a):
        return test_data

    monkeypatch.setattr(CategoryDAL, "get_selection", mock_get_selection)

    response = test_app.get(url='/api/categories/selection/')
    assert response.status_code == 200
    assert response.json() == test_data


def test_update_category(test_app_token: TestClient, monkeypatch):
    test_data = {
        'name': 'Category1'
    }

    test_result = {
        'id': 1,
        'name': 'Category'
    }

    async def mock_get_by_id(self, record_id):
        data = {
            'id': 1,
            'name': test_data['name']
        }
        return Category(**data)

    async def mock_update(self, db_obj, obj_in):
        return Category(**test_result)

    monkeypatch.setattr(CategoryDAL, "get_by_id", mock_get_by_id)
    monkeypatch.setattr(CategoryDAL, "update", mock_update)

    response = test_app_token.put(url='/api/categories/1/', json=test_data)
    assert response.status_code == 200
    assert response.json() == test_result


def test_delete_category(test_app_token: TestClient, monkeypatch):
    test_data = {
        'id': 1,
        'name': 'Category'
    }

    async def mock_get_by_id(self, record_id):
        return Category(**test_data)

    async def mock_delete(self, record_id):
        return

    monkeypatch.setattr(CategoryDAL, "get_by_id", mock_get_by_id)
    monkeypatch.setattr(CategoryDAL, "delete", mock_delete)

    response = test_app_token.delete(url='/api/categories/1/')
    assert response.status_code == 200
    assert response.json() == {'detail': 'OK'}
