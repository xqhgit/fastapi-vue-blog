<template>
  <div class="layout-admin">
    <el-row>
      <el-col :span="4" class="my-col">
        <sidebar />
      </el-col>
      <el-col :span="20">
        <navbar/>
        <app-main />
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Sidebar from './components/Sidebar'
import Navbar from './components/Navbar'
import AppMain from './components/AppMain'

export default {
  name: 'LayoutAdmin',
  components: {
    Sidebar, Navbar, AppMain
  }
}
</script>

<style lang="scss" scoped>
.layout-admin /deep/ {
  .my-col {
    height: 100vh;
    background-color: rgb(84, 92, 100);
  }
}
</style>
