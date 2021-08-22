import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'
// import LayoutAdmin from '@/layout_admin'

Vue.use(Router)

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/index',
    children: [{
      path: 'index',
      name: 'index',
      component: () => import('@/views/IndexPage')
    }, {
      path: 'post',
      name: 'post',
      component: () => import('@/views/PostPage')
    }]
  },
  {
    path: '/admin/login',
    component: () => import('@/views/Admin/LoginPage')
  }
  // {
  //   path: '/admin',
  //   // component: Layout,
  //   children: [{
  //     path: 'login',
  //     name: 'login',
  //     component: () => import('@/views/Admin/LoginPage')
  //   }]
  // }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
