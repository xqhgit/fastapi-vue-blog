<template>
  <div class="app-container">
    <el-form ref="form" v-loading="loading" :model="form" :rules="rules" label-width="80px">
      <el-form-item label="标题" prop="title">
        <el-input v-model="form.title" />
      </el-form-item>
      <el-form-item label="类别" prop="categories">
        <el-select v-model="form.categories" multiple placeholder="请选择" style="width: 100%;">
          <el-option
            v-for="item in categoryOptions"
            :key="item.id"
            :label="item.name"
            :value="item.id"
          />
        </el-select>
      </el-form-item>
      <el-form-item label="简介" prop="description">
        <el-input v-model="form.description" type="textarea" />
      </el-form-item>
      <el-form-item label="主体" prop="body">
        <mavon-editor
          ref="md"
          v-model="form.body"
          :toolbars="toolbars"
          @change="handleMarkdownChange"
          @save="handleEditorSave"
        />
      </el-form-item>
      <el-form-item label="发布" prop="is_published">
        <el-switch v-model="form.is_published" />
      </el-form-item>
      <el-form-item label="评论" prop="can_comment">
        <el-switch v-model="form.can_comment" />
      </el-form-item>
      <el-form-item>
        <el-button v-preventReClick type="primary" @click="onSubmit">保存</el-button>
        <el-button @click="onCancel">返回</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { getCategoriesSelection } from '@/api/category'
import { getPost, updatePost } from '@/api/post'

export default {
  name: 'Create',
  data() {
    return {
      loading: false,
      postId: undefined,
      form: {
        title: undefined,
        categories: undefined,
        description: undefined,
        body: undefined,
        is_published: undefined,
        can_comment: undefined
      },
      rules: {
        title: [
          { required: true, message: '请输入标题', trigger: 'blur' },
          { max: 64, message: '长度在64个字符内', trigger: 'blur' }
        ],
        categories: [
          { required: true, message: '请选择类别', trigger: 'blur' }
        ],
        description: [
          { required: true, message: '请输入简介', trigger: 'blur' }
        ],
        body: [
          { required: true, message: '请编写主体内容', trigger: 'blur' }
        ]
      },
      categoryOptions: [],
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        strikethrough: true, // 中划线
        mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        // imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: true, // 全屏编辑
        readmodel: true, // 沉浸式阅读
        htmlcode: true, // 展示html源码
        help: true, // 帮助
        /* 1.3.5 */
        undo: true, // 上一步
        redo: true, // 下一步
        trash: true, // 清空
        // save: false, // 保存（触发events中的save事件）
        /* 1.4.2 */
        navigation: true, // 导航目录
        /* 2.1.8 */
        alignleft: true, // 左对齐
        aligncenter: true, // 居中
        alignright: true, // 右对齐
        /* 2.2.1 */
        subfield: true, // 单双栏模式
        preview: true // 预览
      }
    }
  },
  mounted() {
    this.getOptionsData()
  },
  methods: {
    getOptionsData() {
      getCategoriesSelection().then(res => {
        this.categoryOptions = res.data
        this.getData()
      })
    },
    getData() {
      this.loading = true
      const postId = this.$route.params.postId
      getPost(postId).then(res => {
        this.form.categories = res.data.categories.map((value, index) => {
          return value['id']
        })
        this.form.id = res.data.id
        this.form.title = res.data.title
        this.form.description = res.data.description
        this.form.body = res.data.body
        this.form.can_comment = res.data.can_comment
        this.form.is_published = res.data.is_published
        this.postId = postId
        this.loading = false
      })
    },
    onSubmit() {
      this.$refs.form.validate((valid) => {
        if (valid) {
          this.loading = true
          updatePost(this.postId, this.form).then(res => {
            this.$message({
              type: 'success',
              message: '修改成功'
            })
            this.loading = false
          })
        }
      })
    },
    onCancel() {
      this.$router.go(-1)
    },
    handleEditorSave(value, render) {
    },
    handleMarkdownChange(value, render) {
    }
  }
}
</script>

<style scoped>

</style>
