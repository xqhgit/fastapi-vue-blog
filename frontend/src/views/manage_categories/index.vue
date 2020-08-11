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
    <create-dialog :visible.sync="openCreate" />
  </div>
</template>

<script>
import CreateDialog from './components/CreateDialog'

export default {
  name: 'ManageCategories',
  components: { CreateDialog },
  data() {
    return {
      row: undefined,
      single: true,
      multiple: true,
      openCreate: false
    }
  },
  methods: {
    handleOpen(name) {
      switch (name) {
        case 'create':
          // this.$router.push({ name: 'manage-categories' })
          break
      }
    }
  }
}
</script>

<style scoped>

</style>
