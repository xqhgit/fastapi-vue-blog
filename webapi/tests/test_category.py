import json
import pytest
from starlette.testclient import TestClient
from webapi.db.dals.category_dal import Category, CategoryDAL


def test_create_category_no_token(test_app: TestClient, monkeypatch):
    data = {
        'name': 'Category1'
    }
    response_data = {
        'name': 'Category1',
        'id': 1
    }

    async def mock_create(a, b):
        return Category(**response_data)

    monkeypatch.setattr(CategoryDAL, "create", mock_create)
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

    async def mock_create(a, b):
        return Category(**response_data)

    monkeypatch.setattr(CategoryDAL, "create", mock_create)
    response = test_app_token.post(url='/api/categories/', json=data)
    assert response.status_code == 201
    assert response.json() == response_data


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

    async def mock_get_all(a):
        return test_data

    monkeypatch.setattr(CategoryDAL, "get_all", mock_get_all)

    response = test_app.get(url='/api/categories/')
    assert response.status_code == 200
    assert response.json() == test_data


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
