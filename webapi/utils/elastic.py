# -*- coding: UTF-8 -*-
from elasticsearch7 import AsyncElasticsearch

from webapi.setting import settings

es = AsyncElasticsearch(hosts=f'{settings.ELASTIC_HOST}:{settings.ELASTIC_PORT}')
INDEX = 'posts'


async def es_search(keyword, page=1, limit=10):
    offset = limit * (page - 1)
    resp = await es.search(
        index=INDEX,
        query={
            "bool": {
                "should": [
                    {
                        "match": {
                            'title': keyword
                        }
                    },
                    {
                        "match": {
                            'description': keyword,
                        }
                    },
                    {
                        "match": {
                            'body': keyword,
                        }
                    }
                ]
            }
        },
        highlight={
            "fields": {
                "title": {},
                "description": {}
            },
            "pre_tags": '<span style="color:red;">',
            "post_tags": '</span>',
            "fragment_size": 10,
        },
        from_=offset,
        size=limit
    )
    return parse_data(resp)


def parse_data(data):
    total = data['hits']['total']['value']
    items = []
    for h in data['hits']['hits']:
        items.append({
            'id': h['_source']['id'],
            'title': h['_source']['title'],
            'description': h['_source']['description'],
            'body': h['_source']['body'],
            'timestamp': h['_source']['timestamp'],
        })
    return {
        'total': total,
        'items': items
    }


async def es_update_doc(data):
    await es_create_doc(data)


async def es_delete_doc(_id):
    await es.delete(
        index=INDEX,
        id=_id,
        ignore=[400, 404]
    )


async def es_create_doc(data):
    await es_delete_doc(data['id'])
    await es.create(
        index=INDEX,
        id=data['id'],
        document=data,
        ignore=[400, 404]
    )
