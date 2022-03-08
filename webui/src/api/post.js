import request from '@/utils/request'

export function getPosts(params) {
  return request({
    url: '/posts/',
    method: 'get',
    params: params
  })
}

export function getPostsPublished(params) {
  return request({
    url: '/posts/published/',
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

export function getPostPublished(postId) {
  return request({
    url: `/posts/published/${postId}/`,
    method: 'get'
  })
}

export function createPost(data) {
  return request({
    url: `/posts/`,
    method: 'post',
    data
  })
}

export function updatePost(recordId, data) {
  return request({
    url: `/posts/${recordId}/`,
    method: 'put',
    data
  })
}

export function deletePost(recordId) {
  return request({
    url: `/posts/${recordId}`,
    method: 'delete'
  })
}

export function searchPostsPublished(params) {
  return request({
    url: '/posts/published/search/',
    method: 'get',
    params: params
  })
}
