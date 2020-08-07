export function getToken() {
  return localStorage.getItem('Token')
}

export function setToken(token) {
  return localStorage.setItem('Token', token)
}

export function removeToken() {
  return localStorage.removeItem('Token')
}
