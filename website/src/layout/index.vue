<template>
  <div>
    <navbar/>
    <br>
    <div class="container">
      <app-main/>
      <br>
      <div id="footer">
        <p>© 2021 by FastAPI-Vue-Blog. All rights reserved. </p>
      </div>
    </div>
  </div>
</template>

<script>
import { Navbar, AppMain } from './components'

export default {
  name: 'Index',
  components: {
    Navbar, AppMain
  }
}
</script>

<style scoped>
  #footer {
    padding: 5px 0px;
    font-size: 80%;
    text-align: right;
    border-top: 1px dotted #88a;
  }
  #footer p {
    margin: 0;
    display: block;
  }
</style>
