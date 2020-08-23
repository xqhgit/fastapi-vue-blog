<template>
  <div>
    <b-pagination
      v-model="currentPage"
      :total-rows="total"
      :per-page="perPage"
      prev-text="Prev"
      next-text="Next"
      aria-controls="categories-card"
      @change="pageChange"
    />
  </div>
</template>

<script>
export default {
  name: 'Pagination',
  props: {
    total: {
      required: true,
      type: Number
    },
    page: {
      type: Number,
      default: 1
    },
    limit: {
      type: Number,
      default: 6
    }
  },
  computed: {
    currentPage: {
      get() {
        return this.page
      },
      set(val) {
        this.$emit('update:page', val)
      }
    },
    perPage: {
      get() {
        return this.limit
      },
      set(val) {
        this.$emit('update:limit', val)
      }
    }
  },
  methods: {
    pageChange(page) {
      this.$emit('pageChange')
    }
  }
}
</script>

<style scoped>

</style>
