import request from '@/utils/request'

export function getCategoriesOptions() {
  return request({
    url: '/categories/options',
    method: 'get'
  })
}

export function uploadAttachment(data) {
  return request({
    url: '/attachments/',
    method: 'post',
    data
  })
}

export function deleteAttachment(data) {
  return request({
    url: '/attachments/',
    method: 'delete',
    data
  })
}

export function createPost(data) {
  return request({
    url: '/posts/admin',
    method: 'post',
    data
  })
}

export function getPost(id) {
  return request({
    url: `/posts/admin/${id}`,
    method: 'get'
  })
}
