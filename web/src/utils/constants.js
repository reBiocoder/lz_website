/*系统中通用常量*/
// icon图标库：  https://material.io/resources/icons/?style=baseline


// 侧边栏相关信息
export const asideList = {
  "manager_home": {
    name: '首页',
    level: 0, //0层，则不能有children变量
    icon: 'home'  //图标
  },
  "manager_system": {
    name: "系统管理",
    level: 1, //层级
    caption: '',
    icon: 'storage',
    children: {  //只允许有两层节点
      'manager_serverInfo': {
        name: "服务器信息",
        level: 0,
        caption: '',
        icon: 'dns'
      }
    }
  },
  "site": {
    name: "网站管理",
    level: 1,
    caption: '',
    icon: 'dvr',
    children: {
      'manager_baseData': {
        name: "基础数据",
        level: 0,
        caption: '',
        icon: 'account_balance'
      },
      'manager_difference_analysis': {
        name: "差异分析",
        level: 0,
        caption: '',
        icon: 'cached'
      },
      'manager_jbrowse': {
        name: "JBrowse",
        level: 0,
        caption: '',
        icon: 'tab'
      }
    }
  }
}








