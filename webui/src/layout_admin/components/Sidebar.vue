<template>
  <div class="sidebar">
    <el-menu
      router
      default-active="/admin/dashboard"
      class="el-menu-vertical-demo"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      @open="handleOpen"
      @close="handleClose">
      <el-menu-item index="/admin/dashboard">
        <i class="el-icon-data-line"/>
        <span slot="title">
          数据统计
        </span>
      </el-menu-item>
      <el-menu-item index="/admin/post">
        <i class="el-icon-document"/>
        <span slot="title">
          文章管理
        </span>
      </el-menu-item>
      <el-menu-item index="/admin/category">
        <i class="el-icon-discount"/>
        <span slot="title">分类管理</span>
      </el-menu-item>
      <el-menu-item index="/admin/comment">
        <i class="el-icon-chat-line-square"/>
        <span slot="title">评论管理</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  mounted() {
    console.log(this.$router)
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style lang="scss" scoped>
.sidebar /deep/ {
  .el-menu-vertical-demo {
    border-right: 0;
  }
}
</style>
