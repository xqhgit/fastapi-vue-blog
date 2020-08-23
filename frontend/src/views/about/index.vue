<template>
  <div>
    <b-jumbotron>
      <template v-slot:header>开源博客</template>

      <template v-slot:lead>
        fastapi-vue-blog 前后端分离开源博客
      </template>

      <hr class="my-4">

      <p>
        后端框架：<br>
        Python Web 框架：FastAPI <br>
        ORM：SQLAlchemy <br>
        前端框架：Vue <br>
        游客界面：BootstrapVue <br>
        管理界面：ElementUI <br>
      </p>

      <b-button variant="primary" href="https://gitee.com/xuqihui/fastapi-vue-blog.git" target="_blank">码云仓库</b-button>
      <!--<b-button variant="success" href="#">Do Something Else</b-button>-->
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  name: 'About',
  created() {
    console.log('About')
  }
}
</script>

<style scoped>

</style>
