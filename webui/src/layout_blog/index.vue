<template>
  <div>
    <navbar style="background-color: #f5f6f9"/>
    <div class="container" style="margin-top: 15px;">
      <app-main/>
    </div>
    <div class="footer">
      <br>
    </div>
  </div>
</template>

<script>
import { Navbar, AppMain } from './components'

export default {
  name: 'LayoutIndex',
  components: {
    Navbar, AppMain
  }
}
</script>

<style scoped>

</style>
