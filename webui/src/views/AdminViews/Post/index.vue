<template>
  <div class="app-container">
    <el-row :gutter="10" class="mb8">
      <el-col :span="14">
        <el-form ref="queryForm" :model="queryParams" :inline="true" label-width="68px" @submit.native.prevent>
          <el-form-item label="" style="margin-bottom: 0">
            <el-input
              v-model="queryParams.title"
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
      :data="rowData"
      :loading="loading"
      :select-row.sync="currentRow"
      :select-rows.sync="currentRows"
      rref="table"
    >
      <el-table-column label="标题" prop="title" />
      <el-table-column label="描述" prop="description">
        <template slot-scope="scope">
          <div v-if="scope.row.description && (scope.row.description.length > 64)">
            <el-popover title="详细" trigger="hover" placement="top" width="400">
              <p style="white-space: pre-wrap; word-break: break-all;">{{ scope.row.description }}</p>
              <div slot="reference">
                <p>{{ scope.row.description | splitDescription }}</p>
              </div>
            </el-popover>
          </div>
          <div v-else>
            <span>{{ scope.row.description }}</span>
          </div>
        </template>
      </el-table-column>
      <el-table-column label="时间" prop="timestamp">
        <template slot-scope="scope">
          <span>{{ scope.row.timestamp.replace('T', ' ') }}</span>
        </template>
      </el-table-column>
      <el-table-column label="类别" prop="categories">
        <template slot-scope="scope">
          <el-tag v-for="n in scope.row.categories" :key="scope.row.id + n" style="margin-right: 5px;" type="success">{{ n }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="评论数" prop="comments" />
      <el-table-column label="可以评论" prop="can_comment">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.can_comment" type="success">是</el-tag>
          <el-tag v-else type="danger">否</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="发布状态" prop="is_published">
        <template slot-scope="scope">
          <el-tag v-if="scope.row.is_published" type="success">已发布</el-tag>
          <el-tag v-else type="danger">未发布</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            v-preventReClick
            size="mini"
            type="text"
            icon="el-icon-edit"
            @click="handleEdit(scope.row)"
          >编辑</el-button>
          <el-divider direction="vertical" />
          <el-dropdown>
            <span class="el-dropdown-link" style="font-size: 12px;">
              更多<i class="el-icon-arrow-down el-icon--right" />
            </span>
            <el-dropdown-menu slot="dropdown">

              <el-dropdown-item>
                <el-button
                  v-preventReClick
                  size="mini"
                  type="text"
                  icon="el-icon-edit-outline"
                  @click="changeCanComment(scope.row)"
                >切换评论</el-button>
              </el-dropdown-item>
              <el-dropdown-item>
                <el-button
                  v-preventReClick
                  size="mini"
                  type="text"
                  icon="el-icon-edit-outline"
                  @click="changeIsPublished(scope.row)"
                >切换发布</el-button>
              </el-dropdown-item>
              <el-dropdown-item>
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
              </el-dropdown-item>
            </el-dropdown-menu>

          </el-dropdown>

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
import { getPosts } from '@/api/post'
import { updatePost, deletePost } from '@/api/post'

export default {
  name: 'Index',
  components: { SelectionTable, Pagination },
  filters: {
    splitDescription: function(value) {
      if (!value) {
        return
      }
      if (value.length > 64) {
        return value.substr(0, 64) + '....'
      }
      return value
    }
  },
  data() {
    return {
      loading: false,
      dataList: [],
      total: 0,
      queryParams: {
        page: 1,
        limit: 10,
        title: undefined
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
      getPosts(this.queryParams).then(res => {
        this.total = res.data.total
        this.rowData = res.data.items
        this.loading = false
      })
    },
    handleCreate() {
      this.$router.push({ 'name': 'PostCreate' })
    },
    handleQuery() {
      this.queryParams.page = 1
      this.queryParams.limit = 10
      this.getData()
    },
    resetQuery() {
      this.queryParams.title = undefined
      this.getData()
    },
    handleEdit(record) {
      this.$router.push({ name: 'PostEdit', params: { postId: record.id }})
    },
    handleDelete(record) {
      this.loading = true
      deletePost(record.id).then(res => {
        this.$message({
          type: 'success',
          message: '删除成功'
        })
        this.getData()
      })
    },
    changeCanComment(record) {
      this.loading = true
      updatePost(record.id, {
        can_comment: !record.can_comment
      }).then(res => {
        this.$message({
          type: 'success',
          message: '修改成功'
        })
        this.getData()
      })
    },
    changeIsPublished(record) {
      this.loading = true
      updatePost(record.id, {
        is_published: !record.is_published
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
.el-dropdown-link {
    cursor: pointer;
    color: #409EFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
</style>
