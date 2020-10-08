import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'

Vue.use(Router)

// export const Routes = [
//   {
//     path: '/',
//     component: Layout,
//     redirect: '/posts',
//     children: [{
//       path: '/login',
//       name: 'login',
//       component: () => import('@/views/login')
//     }, {
//       path: 'posts',
//       name: 'posts',
//       component: () => import('@/views/posts/index')
//     }, {
//       path: 'categories',
//       name: 'categories',
//       component: () => import('@/views/categories/index')
//     }, {
//       path: 'about',
//       name: 'about',
//       component: () => import('@/views/about/index')
//     }, {
//       path: 'manage-posts',
//       name: 'manage-posts',
//       component: () => import('@/views/manage_posts/index')
//     }, {
//       path: 'manage-post',
//       name: 'manage-post',
//       component: () => import('@/views/manage_post/index')
//     }, {
//       path: 'manage-categories',
//       name: 'manage-categories',
//       component: () => import('@/views/manage_categories/index')
//     }]
//   }
// ]

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/posts',
    children: [{
      path: 'posts',
      name: 'posts',
      component: () => import('@/views/posts/index')
    }, {
      path: 'post',
      name: 'post',
      component: () => import('@/views/post/index')
    }, {
      path: 'categories',
      name: 'categories',
      component: () => import('@/views/categories/index')
    }, {
      path: 'about',
      name: 'about',
      component: () => import('@/views/about/index')
    }, {
      path: 'login',
      name: 'login',
      component: () => import('@/views/login')
    }]
  }
]

export const asyncRoutes = [
  {
    path: '/',
    component: Layout,
    children: [{
      path: 'manage-posts',
      name: 'manage-posts',
      component: () => import('@/views/manage_posts/index'),
      meta: { roles: ['admin'] }
    }, {
      path: 'manage-post',
      name: 'manage-post',
      component: () => import('@/views/manage_post/index'),
      meta: { roles: ['admin'] }
    }, {
      path: 'manage-categories',
      name: 'manage-categories',
      component: () => import('@/views/manage_categories/index'),
      meta: { roles: ['admin'] }
    }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
