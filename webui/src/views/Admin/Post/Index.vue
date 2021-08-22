<template>
  <div class="app-container">
    <!--    <el-table-->
    <!--      v-loading="loading"-->
    <!--      ref="table"-->
    <!--      :data="dataList"-->
    <!--      max-height="700"-->
    <!--      highlight-current-row-->
    <!--    >-->
    <!--      <el-table-column label="标题" prop="title" />-->
    <!--      <el-table-column label="描述" prop="title" />-->
    <!--      <el-table-column label="时间" prop="title" />-->
    <!--      <el-table-column label="类别" prop="title" />-->
    <!--      <el-table-column label="评论数" prop="title" />-->
    <!--      <el-table-column label="可以评论" prop="title" />-->
    <!--      <el-table-column label="操作" prop="title" />-->
    <!--    </el-table>-->
    <el-row :gutter="10" class="mb8">
      <el-col :span="14">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px" @submit.native.prevent>
          <el-form-item label="" style="margin-bottom: 0">
            <el-button
              type="primary"
              icon="el-icon-plus"
              size="small"
              @click="handleCreate"
            >新建</el-button>
          </el-form-item>
          <el-form-item label="" style="margin-bottom: 0">
            <el-input
              v-model="queryParams.search"
              clearable
              prefix-icon="el-icon-search"
              size="small"
            />
          </el-form-item>
          <el-form-item style="margin-bottom: 0">
            <el-button type="primary" icon="el-icon-search" size="small" @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="small" @click="resetQuery">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <selection-table
      :data="rowData"
      :loading="loading"
      :select-row.sync="currentRow"
      :select-rows.sync="currentRows"
      rref="table"
    >
      <el-table-column label="标题" prop="title" />
      <el-table-column label="描述" prop="title" />
      <el-table-column label="时间" prop="title" />
      <el-table-column label="类别" prop="title" />
      <el-table-column label="评论数" prop="title" />
      <el-table-column label="可以评论" prop="title" />
      <el-table-column label="操作" prop="title" />
    </selection-table>

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
import SelectionTable from '@/components/SelectionTable'
import Pagination from '@/components/Pagination'

export default {
  name: 'Index',
  components: { SelectionTable, Pagination },
  data() {
    return {
      loading: false,
      dataList: [],
      total: 0,
      queryParams: {
        page: 1,
        limit: 10
      },
      rowData: [],
      currentRow: undefined,
      currentRows: []
    }
  },
  methods: {
    getData() {

    },
    handleCreate() {

    },
    handleQuery() {

    },
    resetQuery() {

    }
  }
}
</script>

<style scoped>

</style>
