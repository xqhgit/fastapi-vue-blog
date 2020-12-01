<template>
  <div class="card mb-3">
    <div class="row no-gutters">
      <div class="col-md-4">
        <img :src="image" class="card-img" alt="...">
      </div>
      <div class="col-md-8" style="background-color: rgb(248, 249, 250)">
        <div class="card-body">
          <h5 class="card-title">
            <span class="badge badge-secondary" style="font-size: 80%;">{{ category }}</span>
            <span class="my-title">
              <router-link :to="{name: 'post', query: {'post_id': postId}}" >{{ title }}</router-link>
            </span>
          </h5>
          <p class="card-text">{{ summary }}</p>
          <p class="card-text"><small class="text-muted">{{ timestamp | getLocalTime }}</small></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PostCard', filters: {
    getLocalTime(nS) {
      const n = nS - (new Date().getTimezoneOffset() * 60)
      const date = new Date(n * 1000)
      return date.toLocaleDateString()
    }
  },
  props: {
    title: {
      type: String,
      required: true
    },
    category: {
      type: String,
      required: true
    },
    image: {
      type: String,
      required: true
    },
    summary: {
      type: String,
      required: true
    },
    timestamp: {
      type: Number,
      required: true
    },
    postId: {
      type: Number,
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
}
/*.card-title:hover {*/
  /*color: black;*/
  /*cursor:pointer;*/
/*}*/
.card-title .my-title >>> a {
  color: black;
  text-decoration:none;
}
.card-title .my-title >>> a:hover {
  color: #17a2b8;
}
</style>
