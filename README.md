# FastAPI Vue Blog博客

[![](https://img.shields.io/badge/Python-3.7-red.svg)](https://www.python.org/downloads)
[![](https://img.shields.io/badge/FastAPI-0.67-yellowgreen.svg)](https://fastapi.tiangolo.com/)
[![](https://img.shields.io/badge/Vue-2.x-green.svg)](https://cn.vuejs.org/index.html)
[![](https://img.shields.io/badge/ElementUI-2.13.2-blue.svg)](https://element.eleme.io/#/zh-CN)
[![](https://img.shields.io/badge/BootstrapVue-2.21.2-blueviolet.svg)](https://code.z01.com/bootstrap-vue/)
[![](https://img.shields.io/badge/Elasticsearch-7.17.0-ff69b4.svg)](https://www.elastic.co/cn/elasticsearch/)


PS: 日常维护中

```
# gitee
https://gitee.com/xuqihui/fastapi-vue-blog

# github
https://github.com/xqhgit/fastapi-vue-blog
```

## 介绍
fastapi-vue-blog Python异步后端实现博客系统

*后端*
* Python Web 框架：FastAPI
* 数据库：MySQL
* ORM：SQLAlchemy
* 搜索：Elasticsearch

*前端*
* 框架：Vue
* 博客界面：BootstrapVue
* 管理界面：ElementUI

### 基本要求
* Python: 3.7.x
* MySQL: 5.7.x
* Node: 12.13.x
* Vue: 2.x

### 功能

*游客*

>1. 可以看到所有文章
>2. 可以看到所有类别
>3. 可以根据分类筛选文章列表
>4. 在文章中可以看到评论
>5. 全文搜索

*管理员*

>1. 数据统计
>2. 文章管理
>3. 类别管理
>4. 评论管理

## 源码下载
```shell
git clone https://gitee.com/xuqihui/fastapi-vue-blog.git
# 或
git clone https://gitee.com/xuqihui/fastapi-vue-blog
```

### 安装
*后端*
```
1: 安装Python 3.7.x，创建虚拟环境
2: 安装MySQL 5.7.x
```
*前端*
```
1: 安装Node版本 12.13.x 和 vue-cli
```

### 开发启动
*后端*
```
# 后端配置数据库和账号密码
1: cd fastapi-vue-blog/webapi
2: 修改setting文件

# 初始化和启动
1: cd fastapi-vue-blog/webapi
2: pip install -r requirements.txt
3: python3 db/init_db.py        # 如果需要初始化数据库
4: python3 app.py
5: http://localhost:8000/docs   # 进入SwaggerUI
```
*前端*
```
1: cd fastapi-vue-blog/webui
2: npm install
3: npm run dev
4: http://localhost:8080        # 进入前端页面
4: http://localhost:8080/admin  # 进入管理员页面
```

## 部署与发布
* 前提：安装好Docker和docker-compose

### 简单发布(可能不适合生产环境)

#### 构建和启动
```
# 工作目录
cd fastapi-vue-blog

# 1.构建镜像并启动服务
docker-compose up -d --build

# 2.初始化数据
docker-compose exec webapp python db/init_db.py
docker-compose restart

# 3.查看服务情况
docker-compose ps
```

#### 其他命令
```
# 1.重启服务
docker-compose restart

# 2.启动服务
docker-compose start <服务名称>

# 3.停止服务
docker-compose stop <服务名称>

# 4.关闭服务并移除容器
docker-compose down
```

## 图片预览

![avatar](./description/index.png)
![avatar](./description/blog.png)
![avatar](./description/mange_login.png)
![avatar](./description/manage_post.png)
![avatar](./description/manage_post_edit.png)
![avatar](./description/create_post.png)
![avatar](./description/manage_category.png)
![avatar](./description/swagger.png)
