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

export function deleteCategory(category_id) {
  return request({
    url: `/categories/${category_id}`,
    method: 'delete'
  })
}
