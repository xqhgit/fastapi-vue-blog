<template>
  <div class="row">
    <!--<h1>Hello World</h1>-->
    <div class="col-md-10">
      <div v-html="contentMD" />
    </div>
    <div class="col-md-2">
      <span/>
    </div>
  </div>
</template>

<script>
// import marked from 'marked'
// import { getPost } from '@/api/post'

export default {
  name: 'PostIndex',
  data() {
    return {
      contentMD: ''
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      // getPost()
    }
  }
}
</script>

<style scoped>

</style>
