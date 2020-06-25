import Vue from 'vue'
import axios from 'axios'
import store from "src/store";
import router from "src/router/index";
// we add it to Vue prototype
// so we can reference it in Vue files
// without the need to import axios
let http = axios.create({
  timeout: 35000,
  baseURL: process.env.http_base_url,
  headers: {'content-type': 'application/x-www-form-urlencoded'},
  withCredentials: true
})

//拦截器
http.interceptors.response.use(function (response) {
  if(response.status !== 200){
    return Promise.reject(new Error("request failed"))
  }
  if(response.data.code === 'login'){//若返回的状态码为登录状态码
    if(response.data.data){ // 返回登陆页面
      window.top.location.href = window.location.origin + '/' + response.data.data['login_url']
    }
    else{
      router.Router.push('/404')
    }
  }
  else{ //正常返回
    return response
  }
})

function _get(url, succ, fail, config = {}) {
  http.get(url, config)
    .then(function (response) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _delete(url, succ, fail, config = {}) {
  http.delete(url, config)
    .then(function (response) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _post(url, param, succ, fail, config = {}) {
  http.post(url, param, config)
    .then(function (response) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _put(url, param, succ, fail, config = {}) {
  http.put(url, param, config)
    .then(function (response) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _getLogo(succ, fail, config = {}) {
  _get('api/config/get_app_logo', succ, fail, config)
}

Vue.prototype.$get = _get
Vue.prototype.$delete = _delete
Vue.prototype.$post = _post
Vue.prototype.$put = _put
Vue.prototype.$logo = _getLogo



