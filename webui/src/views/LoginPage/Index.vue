<template>
  <div class="d-flex justify-content-center">
    <b-form v-if="show" style="width: 500px;" @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="账号:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.email"
          type="email"
          required
        />
      </b-form-group>

      <b-form-group id="input-group-2" label="密码:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.name"
          required
        />
      </b-form-group>
      <b-button type="submit" variant="primary">登陆</b-button>
    </b-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        name: '',
        food: null,
        checked: []
      },
      foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
      show: true
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      alert(JSON.stringify(this.form))
    },
    onReset(evt) {
      evt.preventDefault()
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
