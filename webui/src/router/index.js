import Vue from 'vue'
import Router from 'vue-router'
import Layout from '@/layout'
import LayoutAdmin from '@/layout_admin'

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
  },
  {
    path: '/admin/layout',
    component: () => import('@/layout_admin')
  },
  {
    path: '/admin',
    component: LayoutAdmin,
    redirect: '/admin/dashboard',
    children: [{
      path: 'dashboard',
      name: 'AdminDashboard',
      component: () => import('@/views/Admin/Dashboard')
    }, {
      path: 'post',
      name: 'AdminPost',
      component: () => import('@/views/Admin/Post')
    }, {
      path: 'category',
      name: 'AdminCategory',
      component: () => import('@/views/Admin/Category')
    }, {
      path: 'comment',
      name: 'AdminComment',
      component: () => import('@/views/Admin/Comment')
    }]
  }
]

const createRouter = () => new Router({
  mode: 'history',
  routes: constantRoutes
})

const router = createRouter()
export default router
