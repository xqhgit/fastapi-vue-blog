import request from '@/utils/request'

export function getPosts(query) {
  return request({
    url: '/posts',
    method: 'get',
    params: query
  })
}

export function getCategoriesList() {
  return request({
    url: '/categories/list',
    method: 'get'
  })
}

