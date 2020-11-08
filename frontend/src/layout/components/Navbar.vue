<template>
  <div class="my-navbar" style="background-color: #f8f9fa">
    <b-navbar toggleable="lg" type="light" variant="light" class="container container-fluid">
      <b-navbar-brand href="/posts">开源博客</b-navbar-brand>

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
          <b-nav-item v-if="!name" :to="{name: 'login'}" active-class="active">
            登录
          </b-nav-item>
          <b-nav-item-dropdown v-if="name" right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>管理</em>
            </template>
            <b-dropdown-item :to="{name: 'manage-posts'}" active-class="active">文章</b-dropdown-item>
            <b-dropdown-item :to="{name: 'manage-categories'}" active-class="active">分类</b-dropdown-item>
            <b-dropdown-item href="#">评论</b-dropdown-item>
          </b-nav-item-dropdown>
          <b-nav-item-dropdown v-if="name" right>
            <!-- Using 'button-content' slot -->
            <template v-slot:button-content>
              <em>{{ name }}</em>
            </template>
            <b-dropdown-item href="#">配置</b-dropdown-item>
            <b-dropdown-item href="#" @click="handleLogout">退出</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Navbar',
  data() {
    return {
      username: undefined
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    handleLogout() {
      this.$store.dispatch('user/logout').then(() => {
        this.$router.push({ name: 'posts' })
      }).catch(() => {

      })
    }
  }
}
</script>

<style scoped>
.my-navbar >>> .nav-item a.router-link-exact-active {
  color: #17a2b8;
}
.my-navbar >>> .nav-item a:hover {
  color: #17a2b8;
}
</style>
