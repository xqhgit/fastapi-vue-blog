<template>
  <div class="create-dialog">
    <el-dialog
      :visible.sync="currentVisible"
      :close-on-click-modal="false"
      title="创建分类"
      width="600px"
      @close="reset"
    >
      <el-form ref="form" :model="form" :rules="rules" label-width="80px" >
        <el-row>
          <el-col :span="24">
            <el-form-item label="分类名称" prop="name">
              <el-input v-model="form.name" placeholder="请输入分类名称" clearable />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="简介" prop="description">
              <el-input v-model="form.description" type="textarea" placeholder="简介" clearable />
            </el-form-item>
          </el-col>
          <el-col :span="24">
            <el-form-item label="显示封面" prop="img" >
              <el-upload
                ref="upload"
                :on-change="handleFileChange"
                :on-remove="handleRemoveFile"
                :auto-upload="false"
                :limit="1"
                list-type="picture"
                action="#"
              >
                <el-button size="small" type="primary">点击选择</el-button>
                <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
              </el-upload>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" type="primary" @click="submitForm">确定</el-button>
        <el-button size="small" @click="cancel">取消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { createCategory } from '@/api/categories'

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
        name: undefined,
        description: undefined,
        img: undefined
      },
      rules: {
        name: [{ required: true, trigger: 'blur', message: '不能为空' }],
        description: [{ required: true, trigger: 'blur', message: '不能为空' }],
        img: [{ required: true, trigger: 'blur', message: '不能为空' }]
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
      this.form = {
        name: undefined,
        img: undefined
      }
      this.$refs.upload.clearFiles()
      this.resetForm()
    },
    resetForm() {
      this.$nextTick(() => {
        this.$refs['form'].resetFields()
      })
    },
    handleFileChange(file, fileList) {
      this.form.img = file.raw
    },
    handleRemoveFile(file, fileList) {
      this.form.img = undefined
    },
    cancel() {
      this.currentVisible = false
      this.reset()
    },
    submitForm() {
      this.$refs['form'].validate(valid => {
        if (valid) {
          const data = new FormData()
          data.append('name', this.form.name)
          data.append('img', this.form.img)
          createCategory(data).then(res => {
            this.currentVisible = false
            this.reset()
            this.$emit('callback')
          }).catch(() => {

          })
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
