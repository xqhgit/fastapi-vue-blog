import request from '@/utils/request'

export function getPost(id) {
  return request({
    url: `/posts/${id}`,
    method: 'get'
  })
}
