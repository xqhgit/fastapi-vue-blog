<template>
  <div class="manage-post">
    <el-page-header content="创建文章" @back="goBack"/>
  </div>
</template>

<script>
export default {
  name: 'ManagePost',
  methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>

</style>
