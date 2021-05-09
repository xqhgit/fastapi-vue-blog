<template>
  <div>
    <div class="page-header">
      <h1>新建 文章</h1>
    </div>
    <b-form v-if="show" @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="标题"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="分类" label-for="input-2">
        <b-form-select
          id="input-2"
          v-model="form.category"
          :options="categories"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-3" label="文章">
        <markdown-editor v-model="form.content" :options="{ toolbarItems: ['heading','bold','italic']}" />
      </b-form-group>

      <b-button type="submit" variant="secondary">发布</b-button>
    </b-form>
  </div>
</template>

<script>
import MarkdownEditor from '@/components/MarkdownEditor'

export default {
  name: 'CreatePost',
  components: { MarkdownEditor },
  data() {
    return {
      form: {
        email: '',
        name: '',
        food: null,
        checked: [],
        content: ''
      },
      categories: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(event) {
      event.preventDefault()
      // Reset our form values
      this.form.email = ''
      this.form.name = ''
      this.form.food = null
      this.form.checked = []
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  }
}
</script>

<style scoped>

</style>
