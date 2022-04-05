# -*- coding: UTF-8 -*-
from fastapi.responses import JSONResponse


class BusinessStatusCode:
    """业务状态码"""

    SUCCESS = '0000'
    OTHER_ERR = '9999'

    INSERT_DB_ERR = '9994'
    QUERY_DB_ERR = '9993'
    DELETE_DB_ERR = '9992'
    UPDATE_DB_ERR = '9991'
    OTHER_DB_ERR = '9990'


def BusinessResponse(code=None, data=None, message=None):
    """业务响应"""
    if code is None:
        code = BusinessStatusCode.SUCCESS
    if data is None:
        data = {}
    if message is None:
        message = ''
    return JSONResponse({
        'code': code,
        'data': data,
        'message': message,
    }, status_code=200)
