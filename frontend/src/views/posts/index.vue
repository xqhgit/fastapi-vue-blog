<template>
  <div>
    <div class="row">
      <div class="col-md-8">
        <div class="row">
          <div v-for="i in items" :key="i.id" class="col-md-12">
            <post-card :image="i.image"/>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <!--<div class="list-group">-->
        <!--<a href="#" class="list-group-item list-group-item-action active">-->
        <!--<div class="d-flex w-100 justify-content-between">-->
        <!--<h5 class="mb-1">List group item heading</h5>-->
        <!--<small>3 days ago</small>-->
        <!--</div>-->
        <!--<p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>-->
        <!--<small>Donec id elit non mi porta.</small>-->
        <!--</a>-->
        <!--<a href="#" class="list-group-item list-group-item-action">-->
        <!--<div class="d-flex w-100 justify-content-between">-->
        <!--<h5 class="mb-1">List group item heading</h5>-->
        <!--<small class="text-muted">3 days ago</small>-->
        <!--</div>-->
        <!--<p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>-->
        <!--<small class="text-muted">Donec id elit non mi porta.</small>-->
        <!--</a>-->
        <!--<a href="#" class="list-group-item list-group-item-action">-->
        <!--<div class="d-flex w-100 justify-content-between">-->
        <!--<h5 class="mb-1">List group item heading</h5>-->
        <!--<small class="text-muted">3 days ago</small>-->
        <!--</div>-->
        <!--<p class="mb-1">Donec id elit non mi porta gravida at eget metus. Maecenas sed diam eget risus varius blandit.</p>-->
        <!--<small class="text-muted">Donec id elit non mi porta.</small>-->
        <!--</a>-->
        <!--</div>-->
        <!--<div class="card bg-light mb-3" style="max-width: 18rem;">-->
        <!--<div class="card-header">Header</div>-->
        <!--<div class="card-body">-->
        <!--<h5 class="card-title">Light card title</h5>-->
        <!--<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>-->
        <!--</div>-->
        <!--</div>-->
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
