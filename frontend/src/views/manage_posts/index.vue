<template>
  <div class="manage-posts">
    <h4>文章管理</h4>
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
      <el-col :span="14">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px">
          <el-form-item label="标题" style="margin-bottom: 0">
            <el-input
              v-model="queryParams.title"
              placeholder="请输入标题名称"
              clearable
              size="small"
              prefix-icon="el-icon-search"
            />
          </el-form-item>
          <el-form-item style="margin-bottom: 0">
            <el-button type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索</el-button>
            <el-button icon="el-icon-refresh" size="mini" @click="resetQuery">重置</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
    <el-table
      v-loading="loading"
      ref="table"
      :data="dataList"
      row-key="id"
      highlight-current-row
      @row-click="handleRowClick"
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" align="center"/>
      <el-table-column label="标题" prop="title" />
      <el-table-column label="创建时间" prop="timestamp">
        <template slot-scope="scope">
          <span>{{ scope.row.timestamp | getLocalTime }}</span>
        </template>
      </el-table-column>
      <el-table-column label="评论数" prop="comments_count" />
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ManagePosts',
  filters: {
    getLocalTime(nS) {
      const n = nS - (new Date().getTimezoneOffset() * 60)
      const date = new Date(n * 1000)
      return date.toLocaleDateString()
    }
  },
  data() {
    return {
      row: undefined,
      single: true,
      multiple: true,
      loading: false,
      queryParams: {
        title: undefined
      },
      dataList: [{
        'id': 1,
        'title': 'test title',
        'timestamp': '1267987324',
        'comments_count': 30
      }, {
        'id': 2,
        'title': 'test title2',
        'timestamp': '1267987324',
        'comments_count': 30
      }]
    }
  },
  methods: {
    handleOpen(name) {
      switch (name) {
        case 'create':
          this.$router.push({ name: 'manage-post' })
          break
      }
    },
    handleQuery() {

    },
    resetQuery() {

    },
    handleRowClick(row, column, event) {
      this.$refs['table'].clearSelection()
      this.$refs['table'].toggleRowSelection(row)
      this.row = row
    },
    handleSelectionChange(selection) {
      this.single = selection.length !== 1
      this.multiple = !selection.length
      this.row = undefined
    }
  }
}
</script>

<style scoped>

</style>
