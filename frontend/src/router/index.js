import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'

Vue.use(Router)

export const Routes = [
  {
    path: '/',
    component: Layout,
    redirect: '/posts',
    children: [{
      path: '/login',
      name: 'login',
      component: () => import('@/views/login')
    }, {
      path: 'posts',
      name: 'posts',
      component: () => import('@/views/posts/index')
    }, {
      path: 'categories',
      name: 'categories',
      component: () => import('@/views/categories/index')
    }, {
      path: 'about',
      name: 'about',
      component: () => import('@/views/about/index')
    }, {
      path: 'manage-posts',
      name: 'manage-posts',
      component: () => import('@/views/manage_posts/index')
    }, {
      path: 'manage-post',
      name: 'manage-post',
      component: () => import('@/views/manage_post/index')
    }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: Routes
})

const router = createRouter()
export default router
