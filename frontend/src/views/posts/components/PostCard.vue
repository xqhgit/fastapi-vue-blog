<template>
  <div class="card mb-3">
    <div class="row no-gutters">
      <div class="col-md-4">
        <img :src="image" class="card-img" alt="...">
      </div>
      <div class="col-md-8" style="background-color: rgb(248, 249, 250)">
        <div class="card-body">
          <h5 class="card-title">Card title</h5>
          <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
          <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostCard',
  props: {
    image: {
      type: String,
      required: true
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
}.card-title:hover {
  color: #17a2b8;
  cursor:pointer;
}
</style>
