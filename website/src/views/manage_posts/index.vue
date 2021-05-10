<template>
  <div>
    <div class="page-header">
      <h1>文章
        <span class="float-right"><router-link :to="{name: 'create-post'}" class="btn btn-primary btn-sm">新建文章</router-link></span>
      </h1>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>标题</th>
            <th>类别</th>
            <th>操作</th>
          </tr>
        </thead>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.title }}</td>
          <td>{{ item.category }}</td>
          <td>
            <a class="btn btn-info btn-sm" href="#">编辑</a>
            <a class="btn btn-danger btn-sm" href="#">删除</a>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MangePostsIndex',
  data() {
    return {
      fields: [''],
      items: [
        { id: 40, title: 'Dickerson', category: 'Macdonald' },
        { id: 21, title: 'Larsen', category: 'Shaw' },
        { id: 89, title: 'Geneva', category: 'Wilson' },
        { id: 38, title: 'Jami', category: 'Carney' }
      ]
    }
  }
}
</script>

<style scoped>

</style>
