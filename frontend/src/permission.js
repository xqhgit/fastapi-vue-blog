import router from './router'
import store from './store'
import { Message } from 'element-ui'
import { getToken } from './utils/auth'

const whiteList = ['/login', '/posts', '/post', '/categories', '/about'] // no redirect whitelist

router.beforeEach(async(to, from, next) => {
  const hasToken = getToken()
  if (hasToken) {
    if (to.path === 'login') {
      next({ path: '/' })
    } else {
      const hasRoles = store.getters.roles && store.getters.roles.length > 0
      if (hasRoles) {
        next()
      } else {
        try {
          const { roles } = await store.dispatch('user/getInfo')
          // 根据角色生成路由
          const accessRoutes = await store.dispatch('permission/generateRoutes', roles)
          // 动态添加可访问路由
          router.addRoutes(accessRoutes)
          next({ ...to, replace: true })
        } catch (e) {
          await store.dispatch('user/resetToken')
          Message.error(e || 'Has Error')
          next(`/login?redirect=${to.path}`)
        }
      }
    }
  } else {
    // has no token
    if (whiteList.indexOf(to.path) !== -1) {
      // 如果为白名单url
      next()
    } else {
      next(`/login?redirect=${to.path}`)
    }
  }
})

