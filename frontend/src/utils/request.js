import axios from 'axios'
import store from '@/store'
import { getToken } from '@/utils/auth'
import { MessageBox, Message } from 'element-ui'

// 创建一个axios实例
console.log(process.env)
console.log(process.env.API_URL)
const service = axios.create({
  baseURL: process.env.API_URL,
  timeout: 5000 // 请求超时时间
})

// 设置请求拦截器
service.interceptors.request.use(
  config => {
    if (store.getters.token) {
      config.headers['Authorization'] = 'Bearer ' + getToken()
    }
    return config
  },
  error => {
    console.log(error) // for debug
    return Promise.reject(error)
  }
)
// 设置响应拦截器
service.interceptors.response.use(
  response => {
    console.log(response.data)
    return response
  },
  error => {
    if (error.response.status === 403) {
      MessageBox.confirm('登录状态已过期，您可以继续留在该页面，或者重新登录', '系统提示', {
        confirmButtonText: '重新登录',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        store.dispatch('user/resetToken').then(() => {
          location.reload()
        })
      })
    }
    console.log('err' + error) // for debug
    Message({
      message: error.response.data,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service
