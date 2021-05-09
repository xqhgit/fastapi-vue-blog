<template>
  <div>
    <br>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="用户名:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.username"
          type="text"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="密码:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.password"
          type="password"
          required
        />
      </b-form-group>

      <b-button type="submit" variant="primary">登陆</b-button>
      <b-button type="reset" variant="danger">重置</b-button>
    </b-form>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
// import { login } from ''

export default {
  name: 'LoginIndex',
  data() {
    return {
      form: {
        username: undefined,
        password: undefined
      },
      loading: false,
      show: true
    }
  },
  methods: {
    onSubmit(event) {
      event.preventDefault()
      // alert(JSON.stringify(this.form))
      // this.loading = true
      this.$store.dispatch('user/login', this.form).then(() => {
        // this.$router.push({ path: this.redirect || '/' })
        // this.$router.push({ name: 'Dashboard' })
        // this.loading = false
        alert('登陆成功')
        this.$router.push({ name: 'index' })
      }).catch(() => {
        // this.loading = false
        alert('登陆失败')
      })
    },
    onReset(event) {
      event.preventDefault()
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
