import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'

Vue.use(Router)

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/index',
    children: [{
      path: 'index',
      name: 'index',
      component: () => import('@/views/index/index')
    }, {
      path: 'post',
      name: 'post',
      component: () => import('@/views/post/index')
    }, {
      path: 'login',
      name: 'login',
      component: () => import('@/views/login/index')
    }]
  },
  {
    path: '/manage',
    component: Layout,
    redirect: '/posts',
    children: [{
      path: 'posts',
      name: 'manage-posts',
      component: () => import('@/views/manage_posts/index')
    }, {
      path: 'create-post',
      name: 'create-post',
      component: () => import('@/views/manage_posts/create')
    }]
  }
]

export const asyncRoutes = [
  // {
  //   path: '/manage',
  //   component: Layout,
  //   redirect: '/posts',
  //   children: [{
  //     path: 'posts',
  //     name: 'manage-posts',
  //     component: () => import('@/views/manage_posts/index')
  //   }]
  // }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
