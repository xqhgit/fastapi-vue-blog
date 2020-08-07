import request from '@/utils/request'

export function login(data) {
  const form = new FormData()
  const keys = Object.keys(data)
  keys.forEach(key => {
    form.append(key, data[key])
  })
  return request({
    url: '/login/access-token',
    method: 'post',
    data: form
  })
}

export function getInfo(token) {
  return request({
    url: '/login/getinfo',
    method: 'get'
  })
}

