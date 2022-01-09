<template>
  <b-navbar toggleable="lg" type="light" variant="faded" class="container-fluid">
    <b-navbar-brand :to="{name: 'BlogIndex', query: {page: 1}}">
      <img src="https://placekitten.com/g/30/30" alt="Kitten">
      FastAPI Vue Blog
    </b-navbar-brand>

    <b-navbar-toggle target="nav-collapse" />

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item :to="{name: 'BlogIndex', query: {page: 1}}" active-class="active">
          文章
        </b-nav-item>
        <b-nav-item :to="{name: 'BlogAbout'}" active-class="active">
          关于网站
        </b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav>
        <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="标题关键字" />
          <b-button size="sm" class="my-2 my-sm-0" type="submit">搜索文章</b-button>
        </b-nav-form>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
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

.container-fluid {
  padding-left:  10%;
  padding-right: 10%;
}

</style>
