const getters = {
  name: state => state.user.name,
  token: state => state.user.token,
  roles: state => state.user.roles
}
export default getters
