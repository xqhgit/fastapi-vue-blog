<template>
  <div class="create-dialog">
    <el-dialog
      :visible.sync="currentVisible"
      :close-on-click-modal="false"
      title="创建分类"
      width="600px"
    >
      <el-form ref="form" :model="form" :rules="rules" />
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CreateDialog',
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      form: {

      },
      rules: {

      }
    }
  },
  computed: {
    currentVisible: {
      get() {
        return this.visible
      },
      set(val) {
        this.$emit('update:visible', val)
      }
    }
  }
}
</script>

<style scoped>

</style>
