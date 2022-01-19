<template>
  <div>
    <navbar style="background-color: #f5f6f9" />
    <div class="container" style="margin-top: 15px; height: 100%;">
      <app-main />
      <div class="footer">
        <span>Copyright © 2021 <a href="https://gitee.com/xuqihui/fastapi-vue-blog" target="_blank">FastAPI-Vue-Blog</a> All Rights Reserved.</span>
      </div>
    </div>
  </div>
</template>

<script>
import { Navbar, AppMain } from './components'

export default {
  name: 'LayoutIndex',
  components: {
    Navbar, AppMain
  }
}
</script>

<style scoped>
.footer {
  width: 100%;
  height: 30px;
  line-height: 30px;
  /*position: fixed;*/
  bottom: 0;
  text-align: right;
  color: #6c757d;
  font-size: 12px;
  letter-spacing: 1px;
  border-top: 1px dotted #88a;
}
</style>
