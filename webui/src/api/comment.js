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
