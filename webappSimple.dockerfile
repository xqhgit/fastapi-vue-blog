FROM node:12-buster as buildWeb
WORKDIR /workspace
COPY webui webui

WORKDIR /workspace/webui
RUN npm install
RUN npm run build:prod

FROM python:3.7-buster

RUN echo 'deb http://mirrors.163.com/debian/ stretch main non-free contrib' > /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian/ stretch-updates main non-free contrib' >> /etc/apt/sources.list
RUN echo 'deb http://mirrors.163.com/debian-security/ stretch/updates main non-free contrib' >> /etc/apt/sources.list
RUN apt update
RUN apt install -y libtinfo5 --allow-remove-essential
RUN apt install -y ncurses-base
RUN apt install -y vim

WORKDIR /workspace
COPY webapi webapi

WORKDIR /workspace/webapi
RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install -U setuptools
RUN pip install -r requirements.txt
COPY --from=buildWeb /workspace/webui/dist/static static
COPY --from=buildWeb /workspace/webui/dist/index.html static/

EXPOSE 5000

ENTRYPOINT uvicorn app:app --host 0.0.0.0 --port 5000
