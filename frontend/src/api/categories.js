import request from '@/utils/request'

export function getCategories(query) {
  return request({
    url: '/categories/',
    method: 'get',
    params: query
  })
}

export function createCategory(data) {
  return request({
    url: '/categories/',
    method: 'post',
    data
  })
}
