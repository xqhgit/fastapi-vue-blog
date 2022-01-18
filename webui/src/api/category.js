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

export function deleteCategory(recordId) {
  return request({
    url: `/categories/${recordId}/`,
    method: 'delete'
  })
}

export function getAllCategories(params) {
  return request({
    url: '/categories/',
    method: 'get',
    params: params
  })
}

export function getCategoriesSelection() {
  return request({
    url: '/categories/selection/',
    method: 'get'
  })
}

export function getCategoriesPublished(params) {
  return request({
    url: '/categories/published/',
    method: 'get',
    params: params
  })
}
