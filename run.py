# coding=utf8
import uvicorn
from app import create_app

app = create_app()

if __name__ == '__main__':
    # dev
    uvicorn.run(f'{__name__}:app', port=5000, host='127.0.0.1', reload=True)
    # prod
    # uvicorn.run(app, port=80, host='0.0.0.0', log_config=settings.LOGGING)

