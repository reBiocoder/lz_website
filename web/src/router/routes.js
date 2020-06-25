function load(component) {
  return () => import(`components/${component}.vue`)
}

const routes = [
  {
    path: '/',
    redirect: '/admin/'
  },
  //------后台管理路由-------
  {
    path: '/admin/',
    redirect: '/admin/home',
    component: load('manager/layout'),
    children: [
      // 基础数据配置相关路由
      {path: 'base_data', component: load('manager/base/baseData'), name: 'manager_baseData', meta: {title: '基础数据'}},
      {
        path: 'base_data_change/:code',
        component: load('manager/base/baseDataChange'),
        name: 'manager_baseDataChange',
        meta: {title: '修改基础数据'}
      },
      //后台首页配置
      {path: 'home', component: load('manager/base/home'), name: 'manager_home', meta: {title: '后台管理首页'}},
      //服务器信息配置
      {
        path: 'serverinfo',
        component: load('manager/base/serverinfo'),
        name: 'manager_serverInfo',
        meta: {title: '服务器信息'}
      },
      //差异分析配置
      {
        path: 'difference',
        component: load('manager/base/difference'),
        name: 'manager_difference_analysis',
        meta: {title: '差异分析'}
      },
      //JBrowse tracks配置
      {path: 'jbrowse', component: load('manager/base/jbrowse'), name: 'manager_jbrowse', meta: {title: 'jbrowse配置'}},
      {
        path: 'import_data',
        component: load('manager/base/importExcel'),
        name: 'manager_importExcel',
        meta: {title: '导入数据'}
      },

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
      {path: 'hot', component: load('display/hot'), name: 'hot'},


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
