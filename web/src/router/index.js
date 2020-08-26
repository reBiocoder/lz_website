import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'

Vue.use(VueRouter)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({x: 0, y: 0}),
    routes,

    // Leave these as they are and change in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  //全局验证函数
  Router.beforeEach((to, from, next) => {
    if (to.meta.title) {//修改标题
      document.title = to.meta.title
    }
    if(to.meta.needLogin && !document.cookie){ //若是需要验证的页面，同时没有cookie，则直接重定向到需要登录
     Router.push({name: "login"})
    }
    else{
     next()
    }
  })

  return Router
}
