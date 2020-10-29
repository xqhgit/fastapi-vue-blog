import request from '@/utils/request'

export function getPosts(params) {
  return request({
    url: '/posts/admin',
    method: 'get',
    data: params
  })
}

