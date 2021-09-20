<template>
  <drag-dialog
    v-loading="loading"
    title="创建类别"
    :visible.sync="currentVisible"
    width="500px"
    @close="handleClose"
    @submit="handleSubmit"
    @cancel="handleCancel"
  >
    <el-form ref="form" :model="form" :rules="rules" size="small">
      <el-form-item label="名称" prop="name">
        <el-input v-model="form.name" clearable />
      </el-form-item>
    </el-form>
  </drag-dialog>
</template>

<script>
import { createCategory, updateCategory } from '@/api/category'
import DragDialog from '@/components/DragDialog'

export default {
  name: 'CreateDialog',
  components: { DragDialog },
  props: {
    visible: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      loading: false,
      form: {
        name: undefined
      },
      rules: {
        name: [
          { required: true, message: '请输入类别名称', trigger: 'blur' },
          { max: 32, message: '长度在32个字符内', trigger: 'blur' }
        ]
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
  },
  methods: {
    reset() {
      this.loading = false
      this.form = {
        name: undefined
      }
      this.$nextTick(() => {
        this.$refs['form'].resetFields()
      })
    },
    handleClose() {
      this.currentVisible = false
      this.reset()
    },
    handleCancel() {
      this.currentVisible = false
      this.reset()
    },
    handleSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.loading = true
          if (this.form.recordId === undefined) {
            createCategory(this.form).then(res => {
              this.$message({
                type: 'success',
                message: '创建成功'
              })
              this.handleClose()
              this.$emit('success')
            }).catch(() => {
            })
          } else {
            const data = {
              name: this.form.name
            }
            updateCategory(this.form.recordId, data).then(res => {
              this.$message({
                type: 'success',
                message: '修改成功'
              })
              this.handleClose()
              this.$emit('success')
            }).catch(() => {})
          }
        }
      })
    },
    showData(record) {
      this.currentVisible = true
      this.form.recordId = record.id
      this.form.name = record.name
    }
  }
}
</script>

<style scoped>

</style>
