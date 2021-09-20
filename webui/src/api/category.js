import request from '@/utils/request'

export function createCategory(data) {
  return request({
    url: '/categories/',
    method: 'post',
    data
  })
}

export function updateCategory(recordId, data) {
  return request({
    url: `/categories/${recordId}/`,
    method: 'put',
    data
  })
}

export function getAllCategories(params) {
  return request({
    url: '/categories/',
    method: 'get',
    params: params
  })
}
