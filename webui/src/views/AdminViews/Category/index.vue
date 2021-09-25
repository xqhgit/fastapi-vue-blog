<template>
  <div class="app-container">
    <el-row :gutter="10" class="mb8">
      <el-col :span="14">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px" @submit.native.prevent>
          <el-form-item label="" style="margin-bottom: 0">
            <el-input
              v-model="queryParams.name"
              clearable
              prefix-icon="el-icon-search"
              size="small"
            />
          </el-form-item>
          <el-form-item style="margin-bottom: 0">
            <el-button type="primary" icon="el-icon-search" size="small" plain @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="small" plain @click="resetQuery">重置</el-button>
            <el-button
              type="primary"
              icon="el-icon-plus"
              size="small"
              plain
              @click="handleCreate"
            >新建</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <selection-table
      ref="table"
      :data="rowData"
      :loading="loading"
      :select-row.sync="currentRow"
      :select-rows.sync="currentRows"
    >
      <el-table-column label="名称" prop="name" />
      <el-table-column label="文章数" prop="posts" />
      <el-table-column label="操作" prop="title">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleEdit(scope.row)"
          >编辑</el-button>
          <el-divider direction="vertical" />
          <el-popconfirm
            title="这是一段内容确定删除吗？"
            @onConfirm="handleDelete(scope.row)"
          >
            <el-button
              slot="reference"
              size="mini"
              type="text"
              icon="el-icon-delete"
            >删除</el-button>
          </el-popconfirm>
        </template>
      </el-table-column>
    </selection-table>

    <pagination
      :total="total"
      :page.sync="queryParams.page"
      :limit.sync="queryParams.limit"
      auto-scroll
      @pagination="getData"
    />

    <create-dialog ref="CreateDialog" :visible.sync="createVisible" @success="getData" />
  </div>
</template>

<script>
import { getAllCategories, deleteCategory } from '@/api/category'
import SelectionTable from '@/components/SelectionTable'
import Pagination from '@/components/Pagination'
import CreateDialog from './components/CreateDialog'

export default {
  name: 'Index',
  components: { SelectionTable, Pagination, CreateDialog },
  data() {
    return {
      loading: false,
      dataList: [],
      total: 0,
      queryParams: {
        page: 1,
        limit: 10,
        unlimit: false
      },
      rowData: [],
      currentRow: {},
      currentRows: [],
      createVisible: false
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      this.loading = true
      getAllCategories(this.queryParams).then(res => {
        this.total = res.data.total
        this.rowData = res.data.items
        this.loading = false
      })
    },
    handleCreate() {
      this.$refs['CreateDialog'].createData()
    },
    handleQuery() {
      this.queryParams.page = 1
      this.queryParams.limit = 10
      this.getData()
    },
    resetQuery() {
      this.queryParams.name = undefined
      this.getData()
    },
    handleEdit(row) {
      this.$refs['CreateDialog'].updateData(row)
    },
    handleDelete(row) {
      deleteCategory(row.id).then(res => {
        this.$message({
          type: 'success',
          message: '删除成功'
        })
        this.getData()
      }).catch(() => {})
    }
  }
}
</script>

<style scoped>

</style>
