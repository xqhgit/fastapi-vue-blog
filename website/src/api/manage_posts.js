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

