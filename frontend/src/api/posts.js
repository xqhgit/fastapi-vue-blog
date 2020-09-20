import request from '@/utils/request'

export function getPosts(query) {
  return request({
    url: '/posts',
    method: 'get',
    params: query
  })
}

export function getCategoriesOptions() {
  return request({
    url: '/categories/options',
    method: 'get'
  })
}

export function uploadAttachement(data) {
  console.log('print upload data', data)
  return request({
    url: '/attachments/',
    method: 'post',
    data
  })
}

