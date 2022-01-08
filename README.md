# FastAPI Vue Blog博客
PS: 项目正在开发

##介绍
fastapi-vue-blog Python异步后端实现博客系统

*后端*
* Python Web 框架：FastAPI
* 数据库：MySQL
* ORM：SQLAlchemy
* 搜索：Elasticsearch (未集成)

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
>5. 全文高亮搜索

*管理员*

>1. 数据统计
>2. 文章管理
>3. 类别管理
>4. 评论管理

## 源码下载
```shell
git clone https://gitee.com/xuqihui/fastapi-vue-blog.git
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
通过Docker和Dockerfile打包发布

### 简单发布(可能不适合生产环境)
```
前提：安装好Docker和docker-compose
1: cd fastapi-vue-blog
2: docker-compose -f webappSimple-compose.yml up -d --build
3: docker-compose -f webappSimple-compose.yml exec webapp python db/init_db.py  # 如果数据没有初始化
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
