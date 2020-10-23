import request from '@/utils/request'

export function getCategoriesOptions() {
  return request({
    url: '/posts/admin',
    method: 'get'
  })
}

