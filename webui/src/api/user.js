import request from '@/utils/request'

// export function login(data) {
//   return request({
//     url: '/vue-admin-template/user/login',
//     method: 'post',
//     data
//   })
// }

// export function login(data) {
//   return request({
//     url: '/admin/login/access_token/',
//     method: 'post',
//     data
//   })
// }

export function login(data) {
  const form = new FormData()
  const keys = Object.keys(data)
  keys.forEach(key => {
    form.append(key, data[key])
  })
  return request({
    url: '/admin/login/access_token/',
    method: 'post',
    data: form
  })
}

// export function getInfo(token) {
//   return request({
//     url: '/vue-admin-template/user/info',
//     method: 'get',
//     params: { token }
//   })
// }

export function getInfo() {
  return request({
    url: '/admin/login/getinfo/',
    method: 'get'
  })
}

// export function logout() {
//   return request({
//     url: '/vue-admin-template/user/logout',
//     method: 'post'
//   })
// }
