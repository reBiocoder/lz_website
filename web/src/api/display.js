import Vue from 'vue'

const $post = Vue.prototype.$post
const $get = Vue.prototype.$get

export default {
  index_random_data(cbk) {
    $get('api/index_data/', cbk)
  },
  index_random_col(cbk) {
    $get('api/index_col/', cbk)
  },
  search_data(param, cbk) {
    $post('api/search/', param, cbk)
  },
  search_detail(param, cbk) {
    $post('/api/detail/', param, cbk)
  },
  search_environment(param, cbk) {
    $post('/api/environment/', param, cbk)
  },
  environment_image(param, cbk) {
    $post('/api/get_image/', param, cbk)
  },
  pubmed(param, cbk) {
    $post('/api/pubmed/', param, cbk)
  },
  get_cyano_genomes(cbk) {
    $get('/api/cyano_genomes/', cbk)
  },
  search_cyano_genomes(param, cbk) { //搜索物种数据
    $post('/api/cyano_genomes/', param, cbk)
  },
  global_search(param, cbk) { //全局搜索和搜索产物的结果
    $post('/api/global_search/', param, cbk)
  },
  get_cyano(param, cbk) {  //得到特定基因组的基因
    $post('/api/cyano/', param, cbk)
  },
  get_homolog(param, cbk) {  //得到homologous
    $post('http://124.70.143.103:18882/api/homolog/', param, cbk)
  },
  get_sequence(param, cbk) { //得到序列
    $post('/api/sequence/', param, cbk)
  },
  get_default_sequence(cbk, fail, send_data) { //得到序列
    let base_url = new URL(process.env.http_base_url.toString() + '/api/sequence/')
    base_url.search = new URLSearchParams(send_data)
    $get(base_url.toString(), cbk, fail)
  },
  get_interpro(param, cbk) { //得到互扫描的名称
    $post('/api/interpro/', param, cbk)
  },
  get_kegg(param, cbk) { //得到kegg的代码
    $post('/api/kegg_no/', param, cbk)
  },
}
