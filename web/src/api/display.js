import Vue from 'vue'
const  $post = Vue.prototype.$post
const $get = Vue.prototype.$get

export default {
  index_random_data(cbk){
    $get('api/index_data/',cbk)
  },
  index_random_col(cbk){
    $get('api/index_col/', cbk)
  },
  search_data(param, cbk){
    $post('api/search/', param, cbk)
  },
  search_detail(param, cbk){
    $post('/api/detail/', param, cbk)
  },
  search_environment(param, cbk){
    $post('/api/environment/', param, cbk)
  },
  environment_image(param, cbk){
    $post('/api/get_image/', param, cbk)
  },
  pubmed(param, cbk){
    $post('/api/pubmed/', param, cbk)
  },
  get_cyano_genomes(cbk){
    $get('/api/cyano_genomes/',cbk)
  },
}
