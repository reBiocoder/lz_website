function load(component) {
  return () => import(`components/${component}.vue`)
}

const routes = [
  {
    path: '/',
    redirect: '/lz/'
  },
  //------后台管理路由-------
  {
    path: '/admin/',
    component: load('manager/login_register'),
    redirect: '/admin/login/',
    children: [
      {path: "login/", component: load('manager/login'), name: 'login',meta: {"title": "登录"}},
      {path: "register/", component: load('manager/register'), name: 'register', meta: {"title": "注册"}}
    ]
  },
  {
    path: '/manager/',
    redirect: '/admin/login/',
    component: load('manager/Layout'),
    children: [
      {path: 'user/', component: load('manager/content'), name: 'administrator',meta: {"needLogin": true,"title": '管理中心'}},
      {path: 'csv/', component: load('manager/base/csv'), name: 'csv',meta: {"needLogin": true,"title": '上传csv'}},

    ]
  },
  //----前端用户页面路由------
  {
    path: '/lz/',
    redirect: '/lz/index',
    component: load('display/layout'),
    children: [
      {path: 'index', component: load('display/index'), name: 'index', meta: {title: 'Cyanobacteria Database'}},
      {
        path: 'database/:code',
        component: load('display/detail'),
        props: true,
        name: 'detail',
        meta: {title: 'Detail--Cyanobacteria'}
      },
      {
        path: 'search/:code',
        component: load('display/search'),
        props: true,
        name: 'search',
        meta: {title: 'Search--Cyanobacteria'}
      },
      {path: 'pubmed', component: load('display/pubmed'), name: 'pubmed', meta: {title: 'PubMed'}},
      {path: 'jbrowse', component: load('display/jbrowse'), name: 'jbrowse', meta: {title: 'JBrowse'}},
      {path: 'trending', component: load('display/trending'), name: 'trending'},


    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: load('Error404'),
    name: 'error'
  })
}

export default routes
