import state from './state'
import * as getters from './getters'
import * as mutations from './mutations'
import * as actions from './actions'

import Vue from 'vue'
import Vuex from 'vuex'


let Store = {
  namespaced: true,
  getters,
  mutations,
  actions,
  state
}

Vue.use(Vuex)
Store = new Vuex.Store({
  modules: {[process.env.APP_SCOPE_NAME]: Store},
  strict: process.env.NODE_ENV === 'development'
})

export default Store
