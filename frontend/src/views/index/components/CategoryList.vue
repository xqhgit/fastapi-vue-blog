<template>
  <b-card no-body header="分类">
    <b-list-group flush>
      <template v-for="l in dataList">
        <b-list-group-item :key="l.id" href="#" class="d-flex justify-content-between align-items-center">
          {{ l.name }}
          <b-badge variant="primary" pill>{{ l.count }}</b-badge>
        </b-list-group-item>
      </template>
    </b-list-group>
  </b-card>
</template>

<script>
import { getCategoriesList } from '@/api/posts'

export default {
  name: 'CategoryList',
  data() {
    return {
      dataList: []
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      getCategoriesList().then(res => {
        this.dataList = res.data
      }).catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>

</style>
