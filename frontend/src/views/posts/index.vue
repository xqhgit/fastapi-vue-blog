<template>
  <div>
    <div class="row">
      <div class="col-md-8">
        <div class="row">
          <div v-for="i in items" :key="i.id" class="col-md-12">
            <post-card
              :image="'data:image/jpeg;base64,' + i.cover_image"
              :title="i.title"
              :timestamp="i.timestamp"
              :content="i.content"
            />
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <ul class="list-group">
          <li class="list-group-item d-flex justify-content-between align-items-center">
            python
            <span class="badge badge-primary badge-pill">14</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            flask
            <span class="badge badge-primary badge-pill">2</span>
          </li>
          <li class="list-group-item d-flex justify-content-between align-items-center">
            fastapi
            <span class="badge badge-primary badge-pill">1</span>
          </li>
        </ul>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <pagination :total="total" :page.sync="query.page" :limit.sync="query.limit" auto-scroll @pagination="getData"/>
      </div>
    </div>
  </div>

</template>

<script>
import { getPosts } from '@/api/posts'
import PostCard from './components/PostCard'
import Pagination from '@/components/Pagination'

export default {
  name: 'Posts',
  components: {
    PostCard, Pagination
  },
  data() {
    return {
      total: 0,
      items: [],
      query: {
        page: 1,
        limit: 10
      }
    }
  },
  created() {
    this.getData()
  },
  methods: {
    getData() {
      getPosts(this.query).then(response => {
        this.total = response.data.total
        this.items = response.data.items
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
