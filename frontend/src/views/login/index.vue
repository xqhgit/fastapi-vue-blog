<template>
  <div class="login">
    <!--<h1>登录</h1>-->
    <div class="row" style="margin-top: 100px;">
      <div class="offset-3 col-md-6">
        <el-form ref="form" :model="form" :rules="rules" class="login-form" auto-complete="on" label-position="left">
          <el-form-item label="账号" prop="pass">
            <el-input v-model="form.username" type="teXt" autocomplete="off" clearable />
          </el-form-item>
          <el-form-item label="密码" prop="checkPass">
            <el-input v-model="form.password" type="password" autocomplete="off" clearable />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click.native.prevent="handleLogin">登录</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      form: {
        username: undefined,
        password: undefined
      },
      rules: {
        username: [{ required: true, trigger: 'blur', message: '用户名不能为空' }],
        password: [{ required: true, trigger: 'blur', message: '密码不能为空' }]
      }
    }
  },
  methods: {
    handleLogin() {
      this.$refs['form'].validate(valid => {
        if (valid) {
          this.$store.dispatch('user/login', this.form).then(() => {
            this.$router.push({ name: 'posts' })
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
