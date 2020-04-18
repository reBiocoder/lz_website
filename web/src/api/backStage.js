import Vue from 'vue'
const  $post = Vue.prototype.$post

export default {
  getLogin(param, cbk){
    $post('api/login/', param, cbk)
  },
  getRegister(param, cbk){
    $post('api/register/', param, cbk)
  },
  uploadCsv(param, cbk){
    $post('/api/upload_csv/', param, cbk)
  },
  getColKeys(param, cbk){
    $post('api/get_col_keys/', param, cbk)
  }
}
