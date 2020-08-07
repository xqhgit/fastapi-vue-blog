<template>
  <div class="my-navbar" style="background-color: #f8f9fa">
    <b-navbar toggleable="lg" type="light" variant="light" class="container container-fluid">
      <b-navbar-brand href="#">博客</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"/>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item :to="{name: 'posts'}" active-class="active">
            文章
          </b-nav-item>
          <b-nav-item :to="{name: 'categories'}" active-class="active">
            分类
          </b-nav-item>
          <b-nav-item :to="{name: 'about'}" active-class="active">
            关于网站
          </b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" placeholder="标题关键字"/>
            <b-button size="sm" class="my-2 my-sm-0" type="submit">搜索文章</b-button>
          </b-nav-form>
          <b-nav-item :to="{name: 'login'}" active-class="active">
            登录
          </b-nav-item>
          <!--<b-nav-item-dropdown right>-->
          <!--&lt;!&ndash; Using 'button-content' slot &ndash;&gt;-->
          <!--<template v-slot:button-content>-->
          <!--<em>用户</em>-->
          <!--</template>-->
          <!--<b-dropdown-item href="#">配置</b-dropdown-item>-->
          <!--<b-dropdown-item href="#">退出</b-dropdown-item>-->
          <!--</b-nav-item-dropdown>-->
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
.my-navbar >>> .nav-item a.router-link-exact-active {
  color: #17a2b8;
}
.my-navbar >>> .nav-item a:hover {
  color: #17a2b8;
}
/*.my-navbar >>> .fixed-top {*/
  /*position: sticky;*/
  /*top: 0;*/
  /*right: 0;*/
  /*left: 0;*/
  /*z-index: 1030;*/
  /*margin-bottom: 20px;*/
/*}*/
</style>
