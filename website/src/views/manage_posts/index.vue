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
    <div class="mt-3">
      <b-pagination v-model="currentPage" :total-rows="total" align="right"/>
    </div>
  </div>
</template>

<script>
import { getPostList } from '@/api/manage_posts'

export default {
  name: 'MangePostsIndex',
  data() {
    return {
      fields: [''],
      total: 0,
      items: [],
      currentPage: 1
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      getPostList().then(res => {
        this.total = res.data.total
        this.items = res.data.items
        // this.$bvToast.toast('创建成功', {
        //   title: '通知',
        //   variant: null,
        //   solid: true
        // })
      }).catch(_ => {

      })
    }
  }
}
</script>

<style scoped>

</style>
