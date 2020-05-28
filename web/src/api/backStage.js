import Vue from 'vue'
const  $post = Vue.prototype.$post
const $get = Vue.prototype.$get

export default {
  getLogin(param, cbk){
    $post('api/login/', param, cbk)
  },
  getRegister(param, cbk){
    $post('api/register/', param, cbk)
  },
  uploadCsv(param, cbk){
    $post('api/upload_csv/', param, cbk)
  },
  getColKeys(param,cbk){
    $post('api/get_col_keys/', param, cbk)
  },
  initMenu(cbk) {
    $get('api/init_menu/', cbk)
  },
  get_access(cbk){
    $get("api/get_access/", cbk)
  }
}
