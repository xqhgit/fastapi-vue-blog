# -*- coding: UTF-8 -*-
from elasticsearch7 import AsyncElasticsearch

from webapi.setting import settings

es = AsyncElasticsearch(hosts=f'{settings.ELASTIC_HOST}:{settings.ELASTIC_PORT}')


async def es_search(keyword, page, limit=10):
    offset = limit * (page - 1)
    resp = await es.search(
        index='posts',
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
                "description": {},
                "body_html": {},
            },
            "pre_tags": '<span style="color:red;">',
            "post_tags": '</span>',
            "fragment_size": 10
        },
        from_=offset,
        size=limit
    )
    return parse_data(resp)


def parse_data(data):
    print(data)