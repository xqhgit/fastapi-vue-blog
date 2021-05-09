<template>
  <div id="sidebar">
    <h1>分类</h1>
    <ul>
      <li>
        <a href=""><img src="/static/rss-small.png" alt=""></a>
        <span class="badge badge-info"><a href="#">Python</a></span>
        <span>(10)</span>
      </li>
      <li>
        <a href=""><img src="/static/rss-small.png" alt=""></a>
        <span class="badge badge-info"><a href="#">JavaScript</a></span>
        <span>(2)</span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'Siderbar'
}
</script>

<style scoped>
  #sidebar h1 {
    border-bottom: 1px solid #ccc;
    font-weight: normal;
    font-size: 150%;
  }
  #sidebar ul {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  #sidebar li {
    display: list-item;
    text-align: -webkit-match-parent;
  }
  #sidebar .badge a {
    color: #eee;
    /*text-decoration: none;*/
  }
</style>
