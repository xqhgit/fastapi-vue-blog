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
      path: 'posts',
      name: 'posts',
      component: () => import('@/views/posts/index')
    }]
    // }, {
    //   path: 'about',
    //   name: 'about',
    //   component: () => import('@/views/about/index')
    // }, {
    //   path: 'categories',
    //   name: 'categories',
    //   component: () => import('@/views/categories/index')
    // }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: Routes
})

const router = createRouter()
export default router
