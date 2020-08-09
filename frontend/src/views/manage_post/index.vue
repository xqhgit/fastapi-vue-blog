<template>
  <div class="manage-post">
    <el-page-header content="创建文章" @back="goBack"/>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="标题">
        <el-input v-model="form.name"/>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'ManagePost',
  data() {
    return {
      form: {
        title: undefined
      }
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style scoped>

</style>
