import json
import pytest
from starlette.testclient import TestClient
from webapi.db.dals.post_dal import Post, PostDAL


def test_get_posts(test_app: TestClient, monkeypatch):
    data = {
        "total": 2,
        "items": [
            {
                "id": 1,
                "title": "a",
                "description": "a",
                "timestamp": "2021-09-20T17:03:06",
                "can_comment": True,
                "is_published": True,
                "categories": [
                ],
                "comments": 0
            },
            {
                "id": 2,
                "title": "b",
                "description": "b",
                "timestamp": "2021-09-25T15:02:07",
                "can_comment": True,
                "is_published": True,
                "categories": [
                ],
                "comments": 0
            }
        ]
    }

    async def mock_count(self, title=None):
        return 2

    async def mock_get_limit(self, title=None, *, page, limit):
        d = [
            {
                "id": 1,
                "title": "a",
                "description": "a",
                "timestamp": "2021-09-20T17:03:06",
                "can_comment": True,
                "is_published": True,
            },
            {
                "id": 2,
                "title": "b",
                "description": "b",
                "timestamp": "2021-09-25T15:02:07",
                "can_comment": True,
                "is_published": True,
            }
        ]
        return [Post(**i) for i in d]

    monkeypatch.setattr(PostDAL, "count", mock_count)
    monkeypatch.setattr(PostDAL, "get_limit", mock_get_limit)

    response = test_app.get(url='/api/posts/')
    assert response.status_code == 200
    assert response.json() == data


def test_get_post(test_app: TestClient, monkeypatch):
    data = {
        "id": 1,
        "title": "a",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "body_html": "a",
        "timestamp": "2021-09-20T17:03:06",
        "can_comment": True,
        "is_published": True,
        "categories": [
            {
                "id": 8,
                "name": "Go"
            },
            {
                "id": 13,
                "name": "Python0"
            }
        ],
        "comments": []
    }

    async def mock_get_by_id(self, record_id):
        return data

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    response = test_app.get(url='/api/posts/1/')
    assert response.status_code == 200
    assert response.json() == data


def test_create_post(test_app_token: TestClient, monkeypatch):
    data = {
        "id": 1,
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "body_html": "a",
        "can_comment": True,
        "is_published": True
    }

    create_data = {
        **data,
        "categories": []
    }

    result = {
        "id": 1,
        "title": "test",
    }

    async def mock_get_by_title(self, title):
        return []

    async def mock_create(self, obj_in):
        return Post(**data)

    monkeypatch.setattr(PostDAL, 'get_by_title', mock_get_by_title)
    monkeypatch.setattr(PostDAL, 'create', mock_create)
    response = test_app_token.post(url='/api/posts/', json=create_data)
    assert response.status_code == 201
    assert response.json() == result


def test_create_post_no_token(test_app: TestClient, monkeypatch):
    data = {
        "id": 1,
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "can_comment": True,
        "is_published": True
    }

    create_data = {
        **data,
        "categories": []
    }

    result = {
        "id": 1,
        "title": "test",
    }

    async def mock_get_by_title(self, title):
        return []

    async def mock_create(self, obj_in):
        return Post(**data)

    monkeypatch.setattr(PostDAL, 'get_by_title', mock_get_by_title)
    monkeypatch.setattr(PostDAL, 'create', mock_create)
    response = test_app.post(url='/api/posts/', json=create_data)
    assert response.status_code == 401


def test_update_post(test_app_token: TestClient, monkeypatch):
    data = {
        "id": 1,
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "timestamp": "2021-09-20T17:03:06",
        "can_comment": True,
        "is_published": True
    }

    update_data = {
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "can_comment": True,
        "is_published": True,
        "categories": []
    }

    result = {
        "id": 1,
        "title": "test",
    }

    async def mock_get_by_id(self, title):
        return [1, ]

    async def mock_update(self, db_obj, obj_in):
        return Post(**data)

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(PostDAL, 'update', mock_update)
    response = test_app_token.put(url='/api/posts/1/', json=update_data)
    assert response.status_code == 200
    assert response.json() == result


def test_update_post_no_toke(test_app: TestClient, monkeypatch):
    data = {
        "id": 1,
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "timestamp": "2021-09-20T17:03:06",
        "can_comment": True,
        "is_published": True
    }

    update_data = {
        "title": "test",
        "description": "aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa aaaaaaaaaaaaaaaa",
        "body": "a",
        "can_comment": True,
        "is_published": True,
        "categories": []
    }

    result = {
        "id": 1,
        "title": "test",
    }

    async def mock_get_by_id(self, title):
        return [1, ]

    async def mock_update(self, db_obj, obj_in):
        return Post(**data)

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(PostDAL, 'update', mock_update)
    response = test_app.put(url='/api/posts/1/', json=update_data)
    assert response.status_code == 401


def test_delete_post(test_app_token: TestClient, monkeypatch):
    async def mock_get_by_id(self, title):
        return [1, ]

    async def mock_delete(self, db_obj):
        pass

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(PostDAL, 'delete', mock_delete)
    response = test_app_token.delete(url='/api/posts/1/')
    assert response.status_code == 200


def test_delete_post_no_token(test_app: TestClient, monkeypatch):
    async def mock_get_by_id(self, title):
        return [1, ]

    async def mock_delete(self, db_obj):
        pass

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(PostDAL, 'delete', mock_delete)
    response = test_app.delete(url='/api/posts/1/')
    assert response.status_code == 401
