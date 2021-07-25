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
      component: () => import('@/views/IndexPage')
    }]
  },
  {
    path: '/admin',
    component: Layout,
    children: [{
      path: 'login',
      name: 'login',
      component: () => import('@/views/LoginPage')
    }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
