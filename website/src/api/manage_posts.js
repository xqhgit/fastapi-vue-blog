import request from '@/utils/request'

export function getCategorySelectItems() {
  return request({
    url: '/categories/select_list',
    method: 'get'
  })
}

export function createPost(data) {
  return request({
    url: '/posts/',
    method: 'post',
    data
  })
}

export function getPostList(params) {
  return request({
    url: '/posts/list',
    method: 'get',
    params: params
  })
}

