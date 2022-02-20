<template>
  <div class="app-container">
    <el-row :gutter="10" class="mb8">
      <el-col :span="14">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px" @submit.native.prevent>
          <el-form-item label="" style="margin-bottom: 0">
            <el-input
              v-model="queryParams.search"
              clearable
              prefix-icon="el-icon-search"
              size="small"
            />
          </el-form-item>
          <el-form-item style="margin-bottom: 0">
            <el-button type="primary" icon="el-icon-search" size="small" plain @click="handleQuery">查询</el-button>
            <el-button icon="el-icon-refresh" size="small" plain @click="resetQuery">重置</el-button>
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
      <el-table-column label="ID" prop="id" width="70" />
      <el-table-column label="作者" prop="author" />
      <el-table-column label="邮箱" prop="email" />
      <el-table-column label="内容" prop="body" />
      <el-table-column label="文章" prop="post">
        <template slot-scope="scope">
          <router-link
            target="_blank"
            :to="{name: 'BlogPost', query: {postId: scope.row.post.id}}"
          >
            {{ scope.row.post.title }}
          </router-link>
        </template>
      </el-table-column>
      <el-table-column label="日期" prop="timestamp" width="140">
        <template slot-scope="scope">
          <span>{{ scope.row.timestamp.replace('T', ' ') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="审核通过" prop="reviewed">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.reviewed" type="success">是</el-tag>
          <el-tag v-else type="danger">否</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作" width="160">
        <template slot-scope="scope">
          <el-button
            v-preventReClick
            size="mini"
            type="text"
            icon="el-icon-edit-outline"
            @click="changeReviewed(scope.row)"
          >通过审核</el-button>
          <el-divider direction="vertical" />
          <el-popconfirm
            title="确定评论删除吗？"
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
  </div>
</template>

<script>
import SelectionTable from '@/components/SelectionTable'
import Pagination from '@/components/Pagination'
import { getComments, updateComment, deleteComment } from '@/api/comment'

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
      currentRow: {},
      currentRows: []
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    getData() {
      this.loading = true
      getComments(this.queryParams).then(res => {
        this.total = res.data.total
        this.rowData = res.data.items
        this.loading = false
      })
    },
    handleDelete(record) {
      this.loading = true
      deleteComment(record.id).then(res => {
        this.$message({
          type: 'success',
          message: '删除成功'
        })
        this.getData()
      })
    },
    handleQuery() {
      this.getData()
    },
    resetQuery() {

    },
    changeReviewed(record) {
      this.loading = true
      updateComment(record.id, {
        reviewed: true
      }).then(res => {
        this.$message({
          type: 'success',
          message: '修改成功'
        })
        this.getData()
      })
    }
  }
}
</script>

<style scoped>

</style>
