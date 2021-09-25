import request from '@/utils/request'

export function getPosts(params) {
  return request({
    url: '/posts/',
    method: 'get',
    params: params
  })
}

export function getPost(postId) {
  return request({
    url: `/posts/${postId}`,
    method: 'get'
  })
}
