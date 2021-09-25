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
            },
            {
                "id": 2,
                "title": "b",
                "description": "b",
                "timestamp": "2021-09-25T15:02:07",
                "can_comment": True,
            }
        ]
        return [Post(**i) for i in d]

    monkeypatch.setattr(PostDAL, "count", mock_count)
    monkeypatch.setattr(PostDAL, "get_limit", mock_get_limit)

    response = test_app.get(url='/api/posts/')
    assert response.status_code == 200
    assert response.json() == data
