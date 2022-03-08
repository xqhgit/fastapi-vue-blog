<template>
  <div class="row">
    <div class="col-md-12">
      <div id="main" v-loading="loading">
        <b-alert
          :show="showAlert"
          dismissible
          @dismissed="resetSearch"
        >当前搜索：{{ currentKeyword }}</b-alert>
        <div v-if="dataList.length">
          <div v-for="item in dataList" :key="item.id" class="post">
            <p class="date">{{ item.timestamp | splitDate }}</p>
            <h1 class="post-title">
              <router-link :to="{name: 'BlogPost', query: {postId: item.id}}">
                {{ item.title }}
              </router-link>
            </h1>
            <div class="posted">
              <span>类别：</span>
              <b-badge v-for="category in item.categories" :key="category" style="margin-right: 10px;" variant="info">{{ category }}</b-badge>
            </div>
            <div class="post_body">
              <p style="white-space: pre-wrap; word-break: break-all;">{{ item.description }}</p>
            </div>
            <br>
            <div style="padding-top: 10px;" class="d-flex justify-content-between">
              <router-link
                :to="{name: 'BlogPost', query: {postId: item.id}}"
              >
                继续阅读...
              </router-link>
            </div>
          </div>
          <div class="page">
            <ul class="pager">
              <li class="previous" :class="{disabled: disablePrevious}" @click="handlePrevious"><a href="javascript:;">← 上一页</a></li>
              <li class="next" :class="{disabled: disableNext}" @click="handleNext"><a href="javascript:;">下一页 →</a></li>
            </ul>
          </div>
        </div>
        <div v-else>
          <div style="text-align: center;">
            暂无数据
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { searchPostsPublished } from '@/api/post'

export default {
  name: 'IndexPage',
  filters: {
    splitDate: function(val) {
      return val.split('T')[0]
    }
  },
  data() {
    return {
      loading: false,
      total: 0,
      dataList: [],
      showAlert: false,
      currentKeyword: ''
    }
  },
  computed: {
    disableNext() {
      const query = this.$route.query
      return query.page * 10 >= this.total
    },
    disablePrevious() {
      const query = this.$route.query
      return query.page <= 1
    }
  },
  watch: {
    $route(to, from) {
      this.getData()
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      this.loading = true
      searchPostsPublished(this.$route.query).then(response => {
        this.total = response.data.total
        this.dataList = response.data.items
        this.currentKeyword = this.$route.query.keyword
        this.showAlert = true
      }).finally(() => {
        this.loading = false
      })
    },
    resetSearch() {
      // 返回到首页
      this.$router.push({
        path: '/index',
        query: { page: 1 }
      })
    },
    handleNext() {
      const newQuery = {}
      const oldQuery = this.$route.query
      // 处理page
      if (oldQuery.page === undefined || !/^[0-9]*$/.test(oldQuery.page)) {
        newQuery.page = 1
      } else {
        newQuery.page = parseInt(oldQuery.page) + 1
      }
      // 处理keyword
      newQuery.keyword = oldQuery.keyword
      this.$router.push({
        query: newQuery
      })
    },
    handlePrevious() {
      const newQuery = {}
      const oldQuery = this.$route.query
      // 处理page
      if (oldQuery.page === undefined || !/^[0-9]*$/.test(oldQuery.page)) {
        newQuery.page = 1
      } else {
        newQuery.page = parseInt(oldQuery.page) - 1
      }
      // 处理keyword
      newQuery.keyword = oldQuery.keyword
      this.$router.push({
        query: newQuery
      })
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

    pointer-events: none;
    /*cursor: default;*/
    opacity: 0.6;
  }

  .category-sidebar-bg {
    background-color: #f0f0f0;
    margin-top: 10px;
    height: 100%;
    padding-bottom: 16px;
    padding-top: 16px;
  }
</style>
