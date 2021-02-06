<template>
  <div>
    <navbar/>
    <div class="container">
      <app-main/>
      <div id="footer">
        <p>© 2020-2021 by WorkerXu. All rights reserved. </p>
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
