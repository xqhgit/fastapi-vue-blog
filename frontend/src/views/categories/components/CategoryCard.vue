<template>
  <div>
    <b-card-group columns>
      <b-card
        v-for="i in items"
        :key="i.id"
        :title="title"
        :img-src="i.image"
        img-alt="Image"
        img-top
      >
        <b-card-text>
          <!--This is a wider card with supporting text below as a natural lead-in to additional content.-->
          <!--This content is a little bit longer.-->
          {{ i.content }}
        </b-card-text>
      </b-card>
    </b-card-group>
  </div>
</template>

<script>
export default {
  name: 'PostCard',
  props: {
    items: {
      type: Array,
      default() {
        return []
      }
    }
  }
}
</script>

<style scoped>

</style>
