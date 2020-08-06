# fastapi-vue-blog

#### 介绍
fastapi-vue-blog
前后端分离开源博客
* 后端框架：FastAPI
* 前端框架：Vue (BootstrapVue)


#### 功能

*游客*

>1. 可以看到所有文章
>2. 可以看到所有分类
>3. 可以根据分类筛选文章列表
>4. 在文章中可以看到评论
>5. *可以根据关键词搜索文章

*管理员*

>1. 文章管理
>2. 分类管理
>3. 评论管理
>4. 使用MarkDown编写文章

#### 前端URL

*首页*

* /posts?page=1&limit=10 显示所有文章›
* /post?category=python 分类文章显示
* /posts/<post_id: int> 文章详细

*分类*

* /categories 显示所有分类

#### 后端API

*文章*

* /api/v1/posts/?category=python&page=1&limit=10 显示所有文章 分类文章显示
* /api/v1/posts/<post_id: int> 获取单个文章

*评论*

* /api/v1/comments/ 所有评论
* /api/v1/comments/<comment_id: int> 单个评论
* /api/v1/comments/post/<post_id: int>?page=1&limit=10 文章下的所有评论

*分类*

* /api/v1/categories/ 所有分类
* /api/v1/categories/<category_id: int> 单个分类

*登录*

* /api/v1/login/access-token 登录获取token


#### 后端 

* python版本 3.7.x

1. 在fastapi-vue-blog/backend目录下
2. pip install -r requirements.txt
3. python main.py

#### 前端

* node版本: 12.13.x
* 安装好node和vue-cli

1.  在fastapi-vue-blog/frontend目录下
2.  安装依赖: npm install
3.  启动开发: npm run dev
4.  打包命令: npm run build 

