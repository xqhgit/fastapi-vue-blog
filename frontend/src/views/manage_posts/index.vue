<template>
  <div class="manage-posts">
    <h2>文章管理</h2>
    <el-row :gutter="10" class="mb8">
      <el-col :span="1.5">
        <el-button
          style="margin-top: 5px"
          type="primary"
          icon="el-icon-plus"
          size="mini"
          @click="handleOpen"
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
      v-loding="loading"
      ref="table"
      :data="dataList"
    />
  </div>
</template>

<script>
export default {
  name: 'Index',
  data() {
    return {
      single: false,
      multiple: false,
      loading: false,
      queryParams: {
        title: undefined
      },
      dataList: []
    }
  },
  methods: {
    handleOpen(name) {
      console.log(name)
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
