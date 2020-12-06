<template>
  <div class="post-page">
    <div class="page-header">
      <h1>{{ title }}</h1>
      <small>
        <strong>分类：</strong><a class="badge badge-info" href="#">{{ category }}</a>&nbsp;&nbsp;
        <strong>评论：</strong><span>10</span>&nbsp;&nbsp;
        <strong>日期：</strong><span>{{ timestamp | getLocalTime }}</span>&nbsp;&nbsp;
      </small>
    </div>
    <hr>
    <div class="row page-summary">
      <div class="col-md-12">
        {{ summary }}
      </div>
    </div>
    <div class="row page-content">
      <div class="col-md-12">
        <div class="page-content-img" v-html="content"/>
      </div>
    </div>
    <hr>
    <div class="row page-comments">
      <div class="col-md-12">
        <h3>0 评论</h3>
        <form @submit.prevent="onSubmit">
          <div class="form-group">
            <textarea id="exampleInputEmail1" class="form-control" placeholder="说点什么吧。。。" required />
          </div>
          <button class="btn btn-secondary">评论</button>
        </form>
        <br>
        <ul class="list-group">
          <li class="list-group-item">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">网友1</h5>
              <small data-toggle="tooltip" data-placement="top" data-delay="500" data-timestamp="2020-02-13T09:45:28Z" data-original-title="" title="">
                <span class="" data-timestamp="2020-02-13T09:45:28Z" data-format="fromNow(0)" data-refresh="0" style="">10 months ago</span>
              </small>
            </div>
            <p class="mb-1">好看</p>
            <div class="float-right">
              <a href="javascript:;" class="btn btn-light btn-sm">回复</a>
            </div>
          </li>
          <li class="list-group-item">
            <div class="d-flex w-100 justify-content-between">
              <h5 class="mb-1">网友2</h5>
              <small data-toggle="tooltip" data-placement="top" data-delay="500" data-timestamp="2020-02-13T09:45:28Z" data-original-title="" title="">
                <span class="" data-timestamp="2020-02-13T09:45:28Z" data-format="fromNow(0)" data-refresh="0" style="">10 months ago</span>
              </small>
            </div>
            <p class="alert alert-dark">
              网友1
              <br>
              好看
            </p>
            <p class="mb-1">好看222</p>
            <div class="float-right">
              <a href="javascript:;" class="btn btn-light btn-sm">回复</a>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import marked from 'marked'
import { getPost } from '@/api/post'

export default {
  name: 'PostIndex',
  filters: {
    getLocalTime(nS) {
      const n = nS - (new Date().getTimezoneOffset() * 60)
      const date = new Date(n * 1000)
      return date.toLocaleDateString()
    }
  },
  data() {
    return {
      title: '',
      content: '<div/>',
      summary: '',
      timestamp: '',
      category: ''
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      getPost(parseInt(this.$route.query['post_id'])).then(res => {
        this.title = res.data.title
        this.content = marked(res.data.content)
        this.summary = res.data.summary
        this.timestamp = res.data.timestamp
        this.category = res.data.category
      }).catch(() => {

      })
    },
    onSubmit() {
      alert('Submit')
    }
  }
}
</script>

<style scoped>
.post-page {
  margin-left: 15px;
  margin-right: 15px;
}
.page-content-img >>> img {
  max-width: 100%;
}
</style>
