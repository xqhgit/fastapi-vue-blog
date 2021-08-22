<template>
  <div class="navbar">
    <div class="right-menu">
      <el-dropdown class="avatar-container right-menu-item hover-effect" trigger="click">
        <div class="avatar-wrapper">
          <span class="user-avatar">{{ 'admin' }} <i class="el-icon-caret-bottom" /></span>
        </div>
        <el-dropdown-menu slot="dropdown" class="user-dropdown">
          <router-link to="/profile/index">
            <el-dropdown-item>配置</el-dropdown-item>
          </router-link>
          <el-dropdown-item divided @click.native="logout">
            <span style="display:block;">登出</span>
          </el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Navbar',
  methods: {
    logout({ commit, state }) {
      return Promise.resolve(undefined)
    }
  }
}
</script>

<style lang="scss" scoped>
.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #f5f7fa;
  box-shadow: 0 1px 4px rgba(0, 21, 41, .08);
  justify-content: flex-end;

  //.right-menu {
  //  float: right;
  //  height: 100%;
  //  line-height: 50px;
  //
  //  &:focus {
  //    outline: none;
  //  }
  //
  //  .right-menu-item {
  //    display: inline-block;
  //    padding: 0 8px;
  //    height: 100%;
  //    font-size: 18px;
  //    color: #5a5e66;
  //    vertical-align: text-bottom;
  //
  //    &.hover-effect {
  //      cursor: pointer;
  //      transition: background .3s;
  //
  //      &:hover {
  //        background: rgba(0, 0, 0, .025)
  //      }
  //    }
  //  }
  //
  //  .avatar-container {
  //    margin-right: 30px;
  //
  //    .avatar-wrapper {
  //      margin-top: 5px;
  //      position: relative;
  //
  //      .user-avatar {
  //        cursor: pointer;
  //        width: 40px;
  //        height: 40px;
  //        border-radius: 10px;
  //      }
  //
  //      .el-icon-caret-bottom {
  //        cursor: pointer;
  //        position: absolute;
  //        right: -20px;
  //        top: 25px;
  //        font-size: 12px;
  //      }
  //    }
  //  }
  //}
}
</style>
