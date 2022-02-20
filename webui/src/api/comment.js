import request from '@/utils/request'

export function createComment(data) {
  return request({
    url: '/comments/',
    method: 'post',
    data
  })
}

export function createCommentAnonymous(data) {
  return request({
    url: '/comments/anonymous/',
    method: 'post',
    data
  })
}

export function getComments(params) {
  return request({
    url: '/comments/',
    method: 'get',
    params: params
  })
}

export function updateComment(recordId, data) {
  return request({
    url: `/comments/${recordId}/`,
    method: 'put',
    data
  })
}

export function deleteComment(recordId) {
  return request({
    url: `/comments/${recordId}/`,
    method: 'delete'
  })
}
