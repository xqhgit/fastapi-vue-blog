<template>
  <div>
    <div class="page-header">
      <h1>新建 文章</h1>
    </div>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="标题"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.title"
          type="text"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="分类" label-for="input-2">
        <b-form-select
          id="input-2"
          v-model="form.category_id"
          :options="categories"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-3" label="文章">
        <markdown-editor v-model="form.body" :options="{ toolbarItems: ['heading','bold','italic']}" />
      </b-form-group>

      <b-button type="submit" variant="secondary">发布</b-button>
    </b-form>
  </div>
</template>

<script>
import MarkdownEditor from '@/components/MarkdownEditor'
import { getCategorySelectItems, createPost } from '@/api/manage_posts'

export default {
  name: 'CreatePost',
  components: { MarkdownEditor },
  data() {
    return {
      form: {
        title: undefined,
        category_id: undefined,
        body: undefined
      },
      categories: []
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData(post_id) {
      getCategorySelectItems().then(res => {
        const items = res.data.items
        const result = []
        items.forEach((item, index) => {
          result.push({
            value: item.id,
            text: item.name
          })
        })
        this.categories = result
      })
    },
    onSubmit(event) {
      event.preventDefault()
      createPost(this.form).then(res => {
        this.$bvToast.toast('创建成功', {
          title: '通知',
          variant: null,
          solid: true
        })
        this.$router.push({ name: 'manage-posts' })
      }).catch(_ => {
        this.$bvToast.toast('创建失败', {
          title: '错误',
          variant: 'danger',
          solid: true
        })
      })
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.title = undefined
      this.form.category_id = undefined
      this.form.body = undefined
    }
  }
}
</script>

<style scoped>

</style>
