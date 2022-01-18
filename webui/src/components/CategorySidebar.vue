<template>
  <div class="category-sidebar">
    <h1>类别</h1>
    <ul>
      <li v-for="item in dataList" :key="item.id">
        <span class="badge badge-info">
          <!--          <a :href="`/index?category_id=${item.id}&category_name=${item.name}`">{{ item.name }}</a>-->
          <router-link :to="{name: 'BlogIndex', query: {page: 1, category_id: item.id, category_name: item.name}}">{{ item.name }}</router-link>
        </span>
        <span>({{ item.posts }})</span>
      </li>
    </ul>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { getCategoriesPublished } from '@/api/category'

export default {
  name: 'CategorySidebar',
  data() {
    return {
      dataList: []
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      getCategoriesPublished({ params: { unlimit: true }}).then(res => {
        this.dataList = res.data.items
      })
    }
  }
}
</script>

<style scoped>
  .category-sidebar h1 {
    border-bottom: 1px solid #ccc;
    font-weight: normal;
    font-size: 120%;
  }
  .category-sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  .category-sidebar li {
    display: list-item;
    text-align: -webkit-match-parent;
  }
  .category-sidebar .badge a {
    color: #eee;
    /*text-decoration: none;*/
  }
</style>
