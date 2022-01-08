FROM node:12-buster as buildWeb
WORKDIR /workspace
COPY webui webui

WORKDIR /workspace/webui
RUN npm install
RUN npm run build:prod

FROM python:3.7-buster
WORKDIR /workspace
COPY webapi webapi

WORKDIR /workspace/webapi
RUN pip install -U setuptools
RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
COPY --from=buildWeb /workspace/webui/dist/static static
COPY --from=buildWeb /workspace/webui/dist/index.html static/

EXPOSE 5000

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 5000
