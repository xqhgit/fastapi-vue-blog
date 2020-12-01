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
        <div v-html="content"/>
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
    }
  }
}
</script>

<style scoped>
.post-page {
  margin-left: 15px;
  margin-right: 15px;
}
</style>
