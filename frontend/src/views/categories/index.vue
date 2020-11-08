<template>
  <div
    class="categories"
  >
    <b-card-group
      v-loading="loading"
      columns
      style="min-height: 600px;"
    >
      <b-card
        v-for="i in items"
        :key="i.id"
        :title="i.name"
        :img-src="'data:image/jpeg;base64,' + i.image"
        img-alt="Image"
        img-top
      >
        <b-card-text>
          This is a wider card with supporting text below as a natural lead-in to additional content.
          This content is a little bit longer.
          {{ i.content }}
        </b-card-text>
      </b-card>
    </b-card-group>
    <pagination :total="total" :page.sync="queryParams.page" :limit.sync="queryParams.limit" auto-scroll @pagination="getData" />
  </div>
</template>

<script>
import Pagination from '@/components/Pagination'
import { getCategories } from '@/api/categories'

export default {
  name: 'Categories',
  components: { Pagination },
  data() {
    return {
      loading: false,
      total: 0,
      items: [],
      queryParams: {
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
      this.loading = true
      getCategories(this.queryParams).then(res => {
        this.total = res.data.total
        this.items = res.data.items
        this.loading = false
      })
    }
  }
}
</script>

<style scoped>
.card {
  transition: all 0.5s;
}
.card:hover {
  transform: scale(1.04);
}
.card-img:hover {
  cursor:pointer;
}
.card-title:hover {
  color: #17a2b8;
  cursor:pointer;
}
</style>
