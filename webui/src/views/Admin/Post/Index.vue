<template>
  <div class="app-container">

    <el-table
      v-loading="loading"
      ref="table"
      :data="dataList"
      max-height="700"
      highlight-current-row
    >
      <el-table-column label="标题" prop="title" />
      <el-table-column label="描述" prop="title" />
      <el-table-column label="时间" prop="title" />
      <el-table-column label="类别" prop="title" />
      <el-table-column label="评论数" prop="title" />
      <el-table-column label="可以评论" prop="title" />
      <el-table-column label="操作" prop="title" />
    </el-table>
    <pagination
      :total="total"
      :page.sync="queryParams.page"
      :limit.sync="queryParams.limit"
      auto-scroll
      @pagination="getData"
    />
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'

export default {
  name: 'Index',
  components: { Pagination },
  data() {
    return {
      loading: false,
      dataList: [],
      total: 0,
      queryParams: {
        page: 1,
        limit: 10
      }
    }
  },
  methods: {
    getData() {

    }
  }
}
</script>

<style scoped>

</style>
