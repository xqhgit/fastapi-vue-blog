# fastapi-vue-blog

## 项目在开发阶段

#### 介绍
fastapi-vue-blog
Python异步后端实现博客系统

* 后端框架：
>1. Python Web 框架：FastAPI
>2. ORM：SQLAlchemy
>3. 搜索：Elasticsearch

* 前端框架：Vue
>1. 博客界面：BootstrapVue
>2. 管理界面：ElementUI

#### 启动 

*后端*

* python版本 3.7.x

>1. 在fastapi-vue-blog/webapi目录下
>2. pip install -r requirements.txt
>3. python app.py

*前端*

* node版本: 12.13.x
* 安装好node和vue-cli

>1.  在fastapi-vue-blog/webapi目录下
>2.  安装依赖: npm install
>3.  启动开发: npm run dev


#### 功能

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

#### 插图

![avatar](./description/index.png)
![avatar](./description/blog.png)
![avatar](./description/mange_login.png)
![avatar](./description/manage_category.png)
