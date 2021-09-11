<template>
  <div class="row">
    <div class="col-md-8">
      <div id="main">
        <b-alert show>默认通知</b-alert>
        <div class="post">
          <p class="date">January 11 2021</p>
          <h1 class="post-title">
            <a href="#">
              Beautiful Interactive Tables for your Flask Templates
            </a>
          </h1>
          <div class="posted">
            <span>类别：</span>
            <b-badge variant="info">Python</b-badge>,
            <b-badge variant="info">JavaScript</b-badge>.
          </div>
          <div class="post_body">
            Rendering a table with data in a Flask template is a relatively simple task when
            the table is short, but can be incredibly hard for larger tables that require
            features such as sorting, pagination and searching. In this article I'm going
            to show you how to integrate the dataTables.js library in your templates,
            which will allow you to create fully featured tables with ease!
          </div>
          <div style="padding-top: 10px;" class="d-flex justify-content-between">
            <a href="#">4 个评论</a>
            <a href="#">继续阅读...</a>
          </div>
        </div>
        <div class="page">
          <ul class="pager">
            <li class="previous disabled"><a href="#">← 上一页</a></li>
            <li class="next"><a href="#">下一页 →</a></li>
          </ul>
        </div>
      </div>
    </div>
    <div class="col-md-4 category-sidebar-bg">
      <category-sidebar />
    </div>
  </div>

</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
// import { getPosts } from '@/api/posts'
import CategorySidebar from '@/components/CategorySidebar'
// import PostCard from './components/PostCard'
// import CategoryList from './components/CategoryList'
// import Pagination from '@/components/Pagination'

export default {
  name: 'IndexPage',
  components: {
    CategorySidebar
  },
  data() {
    return {
      total: 0,
      items: [],
      query: {
        page: 1,
        limit: 10
      }
    }
  },
  created() {
    console.log('index')
    this.getData()
  },
  methods: {
    getData() {
      // getPosts(this.query).then(response => {
      //   this.total = response.data.total
      //   this.items = response.data.items
      // })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  /*div {*/
    /*display: block;*/
  /*}*/
  #main {
    padding: 10px 10px 10px 10px;
  }

  #main .date {
    padding: 2px 8px;
    margin: 5px 0px 0px 0px;
    border: 1px solid #ccc;
    font-size: 100%;
    color: #666;
    float: right;
    display: inline;
    position: relative;
    top: 4px;
  }
  #main h1 {
    font-size: 170%;
    font-weight: normal;
    line-height: 140%;
    padding-bottom: 5px;
    margin-top: 20px;
  }

  #main p {
    font-size: 120%;
    line-height: 150%;
    margin-bottom: 20px;
  }
  #main .post {
    margin-bottom: 20px;
  }
  /*main h1.post-title {*/
  /*  color: #666;*/
  /*  padding-bottom: 0;*/
  /*  margin-bottom: 0;*/
  /*}*/
  #main h1.post-title a {
    color: #666;
    cursor:pointer;
    text-decoration:none;
  }
  #main h1.post-title a:hover {
    color: black;
  }
  #main .posted {
    font-size: 100%;
    font-weight: normal;
    padding-bottom: 4px;
    margin-bottom: 16px;
    border-bottom: 1px solid #ccc;
  }
  #main .post_more a {
    color: #66a;
  }
  #main .posted span a {
    color: #eee;
  }

  #main .page {
    border-top: 1px solid #ddd;
  }
  .pager {
    padding-left: 0;
    margin: 20px 0;
    text-align: center;
    list-style: none;
    display: block;
    overflow: auto;
  }
  .pager li {
    padding-left: 0;
    margin: 20px 0;
    text-align: center;
    list-style: none;
    display: inline;
  }
  .pager li>a {
    color: #66a;
    display: inline-block;
    padding: 5px 14px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 15px;
    text-decoration:none;
  }
  .pager li>a:hover {
    color: black;
    background-color: #f0f0f0;
  }
  .pager .previous>a {
    float: left;
  }
  .pager .next>a {
    float: right;
  }
  .pager .disabled>a {
    color: #777;
    cursor: not-allowed;
    background-color: #fff;
  }

  .category-sidebar-bg {
    background-color: #f0f0f0;
    margin-top: 10px;
    height: 100%;
    padding-bottom: 16px;
    padding-top: 16px;
  }
</style>
