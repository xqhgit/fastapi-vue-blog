import json
import pytest
from starlette.testclient import TestClient
from webapi.db.dals.post_dal import Post, PostDAL
from webapi.db.dals.comment_dal import Comment, CommentDAL


def test_create_comment(test_app_token: TestClient, monkeypatch):
    data = {
        'post_id': 1,
        'body': '123'
    }

    result = {
        'detail': 'OK'
    }

    async def mock_get_by_id(self, record_id):
        return [1, ]

    async def mock_create(self, obj_in):
        return Comment(**data)

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(CommentDAL, 'create', mock_create)
    response = test_app_token.post(url='/api/comments/', json=data)
    assert response.status_code == 201
    assert response.json() == result


def test_create_comment_no_token(test_app: TestClient, monkeypatch):
    data = {
        'post_id': 1,
        'body': '123'
    }

    result = {
        'detail': 'OK'
    }

    async def mock_get_by_id(self, record_id):
        return [1, ]

    async def mock_create(self, obj_in):
        return Comment(**data)

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(CommentDAL, 'create', mock_create)
    response = test_app.post(url='/api/comments/', json=data)
    assert response.status_code == 401


def test_create_comment_anonymous(test_app: TestClient, monkeypatch):
    data = {
        'post_id': 1,
        'body': '123',
        'author': 'test',
        'email': 'email@qq.com'
    }
    result = {
        'detail': 'OK'
    }

    async def mock_get_by_id(self, record_id):
        return [1, ]

    async def mock_create(self, obj_in):
        return Comment(**data)

    monkeypatch.setattr(PostDAL, 'get_by_id', mock_get_by_id)
    monkeypatch.setattr(CommentDAL, 'create', mock_create)
    response = test_app.post(url='/api/comments/anonymous/', json=data)
    assert response.status_code == 201
    assert response.json() == result
