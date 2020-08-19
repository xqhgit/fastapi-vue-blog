<template>
  <div class="manage-categories">
    <h4>分类管理</h4>
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          style="margin-top: 5px"
          type="primary"
          icon="el-icon-plus"
          size="mini"
          @click="handleOpen('create')"
        >新增</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          :disabled="single"
          style="margin-top: 5px"
          type="success"
          icon="el-icon-edit"
          size="mini"
          @click="handleOpen"
        >编辑</el-button>
      </el-col>
      <el-col :span="1.5">
        <el-button
          :disabled="multiple"
          style="margin-top: 5px"
          type="danger"
          icon="el-icon-delete"
          size="mini"
          @click="handleOpen"
        >删除</el-button>
      </el-col>
    </el-row>
    <el-table
      ref="table"
      :v-loading="loading"
      :data="dataList"
      max-height="700"
      row-key="id"
      highlight-current-row
      @row-click="handleRowClick"
      @selection-change="handleSelectionChange"
      @sotr-change="handleSortChange"
      @filter-change="handleFilterChange"
    >
      <el-table-column type="selection" align="center" />
      <el-table-column label="分类名称" prop="name" sortable="custom" />
      <el-table-column label="封面图片" prop="img" >
        <template slot-scope="scope">
          <img :src="'data:image/jpeg;base64,' + scope.row.image" class="card-img" alt="...">
        </template>
      </el-table-column>
      <el-table-column label="创建时间" prop="timestamp" sortable="custom" >
        <template slot-scope="scope">
          <span>{{ scope.row.timestamp | getLocalTime }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文章数量" prop="post_count" />
    </el-table>
    <create-dialog ref="createDialog" :visible.sync="openCreate" @callback="getData" />
  </div>
</template>

<script>
import CreateDialog from './components/CreateDialog'
import { getCategories } from '@/api/categories'

export default {
  name: 'ManageCategories',
  components: { CreateDialog },
  filters: {
    getLocalTime(nS) {
      const n = nS - (new Date().getTimezoneOffset() * 60)
      const date = new Date(n * 1000)
      return date.toLocaleDateString()
    }
  },
  data() {
    return {
      categoryIds: [],
      loading: false,
      row: undefined,
      single: true,
      multiple: true,
      openCreate: false,
      dataList: []
    }
  },
  created() {
    this.getData()
  },
  methods: {
    handleOpen(name) {
      switch (name) {
        case 'create':
          this.openCreate = true
          break
      }
    },
    getData() {
      this.loading = true
      getCategories(this.queryParams).then(res => {
        this.dataList = res.data.items
        this.loading = false
      })
    },
    handleRowClick(row, column, event) {
      this.$refs['table'].clearSelection()
      this.$refs['table'].toggleRowSelection(row)
      this.row = row
    },
    handleSelectionChange(selection) {
      this.categoryIds = selection.map(item => item.id)
      this.single = selection.length !== 1
      this.multiple = !selection.length
      this.row = undefined
    },
    handleSortChange(column) {
      this.queryParams.order = column['prop'] + ':' + column['order']
      this.getData()
    },
    handleFilterChange(filters) {
      this.queryParams.filters = Object.assign(this.queryParams.filters, filters)
      this.getData()
    }
  }
}
</script>

<style scoped>

</style>
