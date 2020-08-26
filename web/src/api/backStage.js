import Vue from 'vue'

const $post = Vue.prototype.$post
const $get = Vue.prototype.$get

export default {
  getLogin(param, cbk) {
    $post('api/login/', param, cbk)
  },
  getRegister(param, cbk) {
    $post('api/register/', param, cbk)
  },
  uploadCsv(param, cbk) {
    $post('api/upload_csv/', param, cbk)
  },
  getColKeys(param, cbk) {
    $post('api/get_col_keys/', param, cbk)
  },
  get_access(cbk) {
    $get("api/get_access/", cbk)
  },
  update_utex_tss_data(param, cbk) {
    $post('api/update_tss_utex/', param, cbk)
  },
  uploadexcel(param, cbk) {
    $post('api/import_excel/', param, cbk)
  },

}
