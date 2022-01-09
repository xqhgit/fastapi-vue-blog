<template>
  <div>
    <b-jumbotron>
      <h1 class="display-4">FastAPI-Vue-Blog</h1>
      <p class="lead">Author: Hendy.xu</p>
      <hr class="my-4">
      <p>联系方式</p>
      <p>QQ：1104440778</p>
      <p>邮箱：1104440778@qq.com</p>
      <p>Gitee：<a href="https://gitee.com/xuqihui" target="_blank">https://gitee.com/xuqihui</a></p>
      <b-button variant="primary" href="https://gitee.com/xuqihui/fastapi-vue-blog" target="_blank">项目Gitee仓库</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  name: 'About',
  created() {
    console.log('About')
  }
}
</script>

<style scoped>

</style>
