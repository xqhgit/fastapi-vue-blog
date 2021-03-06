import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'
import BlogLayout from '@/layout_blog'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'/'el-icon-x' the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/',
    component: BlogLayout,
    redirect: '/index',
    hidden: true,
    children: [{
      path: 'index',
      name: 'BlogIndex',
      component: () => import('@/views/BlogViews/IndexPage/index')
    }, {
      path: 'post',
      name: 'BlogPost',
      component: () => import('@/views/BlogViews/PostPage/index')
    }, {
      path: 'search',
      name: 'SearchPost',
      component: () => import('@/views/BlogViews/SearchPage/index')
    }, {
      path: 'about',
      name: 'BlogAbout',
      component: () => import('@/views/BlogViews/AboutPage/index')
    }]
  },
  {
    path: '/login',
    // component: () => import('@/views/AdminViews/Login/index'),
    component: () => import('@/views/AdminViews/Login/index_new'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  }

]

/**
 * asyncRoutes
 * the routes that need to be dynamically loaded based on user roles
 */
export const asyncRoutes = [
  {
    path: '/admin',
    redirect: '/admin/dashboard',
    hidden: true
  },
  {
    path: '/admin/dashboard',
    component: Layout,
    redirect: '/admin/dashboard/index',
    children: [{
      path: 'index',
      name: 'Dashboard',
      component: () => import('@/views/AdminViews/Dashboard/index'),
      meta: { title: '????????????', icon: 'dashboard' }
    }]
  },

  {
    path: '/admin/post',
    component: Layout,
    redirect: '/admin/post/index',
    children: [{
      path: 'index',
      name: 'PostIndex',
      component: () => import('@/views/AdminViews/Post/index'),
      meta: { title: '????????????', icon: 'el-icon-document' }
    }, {
      path: 'create',
      name: 'PostCreate',
      component: () => import('@/views/AdminViews/Post/create'),
      meta: { title: '????????????' },
      hidden: true
    }, {
      path: 'edit/:postId',
      name: 'PostEdit',
      component: () => import('@/views/AdminViews/Post/edit'),
      meta: { title: '????????????' },
      hidden: true
    }]
  },

  {
    path: '/admin/category',
    component: Layout,
    redirect: '/admin/category/index',
    children: [{
      path: 'index',
      name: 'Category',
      component: () => import('@/views/AdminViews/Category/index'),
      meta: { title: '????????????', icon: 'el-icon-discount' }
    }]
  },

  {
    path: '/admin/comment',
    component: Layout,
    redirect: '/admin/comment/index',
    children: [{
      path: 'index',
      name: 'Comment',
      component: () => import('@/views/AdminViews/Comment/index'),
      meta: { title: '????????????', icon: 'el-icon-chat-line-square' }
    }]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
