<template>
  <div class="create-dialog">
    <el-dialog
      v-dialogDrag
      :title="title"
      :visible.sync="currentVisible"
      :width="width"
      append-to-body
      :close-on-click-modal="false"
      @close="handleClose"
    >
      <slot />
      <div slot="footer" class="dialog-footer">
        <el-button v-preventReClick size="small" type="primary" @click="handleSubmit">确定</el-button>
        <el-button size="small" @click="handleCancel">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'DragDialog',
  props: {
    visible: {
      type: Boolean,
      default: false
    },
    title: {
      type: String,
      required: true
    },
    width: {
      type: String,
      default: '800px'
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
  },
  methods: {
    handleClose() {
      this.$emit('close')
    },
    handleCancel() {
      this.$emit('cancel')
    },
    handleSubmit() {
      this.$emit('submit')
    }
  }
}
</script>

<style scoped>

</style>
