<template>
  <div class="manage-post">
    <el-page-header content="创建文章" @back="goBack"/>
    <el-form ref="form" :model="form" :rules="rules" label-width="80px" style="margin-top: 20px">
      <el-row>
        <el-col :span="24">
          <el-form-item label="标题" prop="title">
            <el-input v-model="form.title" clearable />
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="分类" prop="category_id">
            <el-select v-model="form.category_id" placeholder="请选择" clearable >
              <el-option
                v-for="item in categoryOptions"
                :key="item.id"
                :label="item.name"
                :value="item.id"
              />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="发布" prop="is_publish">
            <el-radio-group v-model="form.is_publish" style="margin-top: 6px">
              <el-radio v-for="dict in boolOptions" :key="dict.value" :label="dict.value">{{ dict.label }}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
        <el-col :span="6">
          <el-form-item label="可以评论" prop="can_comment">
            <el-radio-group v-model="form.can_comment" style="margin-top: 6px">
              <el-radio v-for="dict in boolOptions" :key="dict.value" :label="dict.value">{{ dict.label }}</el-radio>
            </el-radio-group>
          </el-form-item>
        </el-col>
        <el-col :span="24">
          <el-form-item label="概要" prop="summary">
            <el-input v-model="form.summary" type="textarea"/>
          </el-form-item>
        </el-col>
        <el-col :span="24">
          <el-form-item label="封面" prop="cover_image">
            <el-upload
              :on-change="handleCoverImageChange"
              :on-remove="handleRemoveCoverImage"
              :auto-upload="false"
              :limit="1"
              list-type="picture"
              action="#"
            >
              <el-button size="small" type="primary">点击选择</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件</div>
            </el-upload>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item>
        <mavon-editor
          ref="md"
          v-model="form.content"
          @change="handleMarkdownChange"
          @save="handleEditorSave"
          @imgAdd="imgAdd"
          @imgDel="imgDel"
        />
      </el-form-item>
      <el-form-item>
        <el-button
          style="margin-top:5px;"
          type="primary"
          icon="el-icon-document"
          @click="handleSave">
          保存
        </el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { getCategoriesOptions, uploadAttachment, deleteAttachment, createPost, getPost } from '@/api/manage_post'

export default {
  name: 'ManagePost',
  data() {
    return {
      post_id: undefined,
      form: {
        title: undefined,
        is_publish: false,
        can_comment: true,
        category_id: undefined,
        cover_image: undefined,
        summary: '',
        content: ''
      },
      rules: {
        title: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        is_publish: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        can_comment: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        category_id: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        cover_image: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        summary: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ],
        content: [
          { required: true, message: '不能为空', trigger: 'blur' }
        ]
      },
      categoryOptions: [],
      boolOptions: [
        { label: '是', value: true },
        { label: '否', value: false }
      ]
    }
  },
  created() {
    getCategoriesOptions().then(res => {
      this.categoryOptions = res.data
    })
    if (this.$route.query.post_id) {
      this.post_id = parseInt(this.$route.query.post_id)
      getPost(this.post_id).then(res => {
        this.form.title = res.data.title
        this.form.category_id = res.data.category_id
        this.form.summary = res.data.summary
        this.form.content = res.data.content
        this.form.is_publish = res.data.is_publish
        this.form.can_comment = res.data.can_comment
      }).catch(() => {})
    }
  },
  methods: {
    goBack() {
      this.$router.go(-1)
    },
    handleEditorSave(value, render) {
    },
    handleMarkdownChange(value, render) {
    },
    imgAdd(filename, imgfile) {
      const data = new FormData()
      data.append('file', imgfile)
      uploadAttachment(data).then(res => {
        const data = res.data
        this.$refs.md.$img2Url(filename, data.url)
      }).catch(() => {

      })
    },
    imgDel(filename) {
      const file_url = filename[0]
      deleteAttachment({ 'url': file_url }).then(res => {
      }).catch((err) => {
        console.log(err)
      })
    },
    handleCoverImageChange(file, fileList) {
      this.form.cover_image = file.raw
    },
    handleRemoveCoverImage(file, fileList) {
      this.form.cover_image = undefined
    },
    handleSave() {
      if (this.post_id === undefined) {
        this.$refs['form'].validate(valid => {
          if (valid) {
            const data = new FormData()
            data.append('title', this.form.title)
            data.append('can_comment', this.form.can_comment)
            data.append('is_publish', this.form.is_publish)
            data.append('category_id', this.form.category_id)
            data.append('cover_image', this.form.cover_image)
            data.append('summary', this.form.summary)
            data.append('content', this.form.content)
            createPost(data).then(res => {
              this.$message({
                type: 'success',
                message: '成功'
              })
              this.goBack()
            }).catch(() => {
              this.$message({
                type: 'error',
                message: '失败'
              })
            })
          }
        })
      } else {
        console.log('admin edit post')
      }
    }
  }
}
</script>

<style scoped>

</style>
