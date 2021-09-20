<template>
  <div class="category-sidebar">
    <h1>类别</h1>
    <ul>
      <li>
        <span class="badge badge-info"><a href="#">Python</a></span>
        <span>(10)</span>
      </li>
      <li>
        <span class="badge badge-info"><a href="#">JavaScript</a></span>
        <span>(2)</span>
      </li>
    </ul>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
export default {
  name: 'CategorySidebar'
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
