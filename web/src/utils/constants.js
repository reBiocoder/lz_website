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
      },
      'manager_importExcel': {
        name: "导入数据",
        level: 0,
        caption: '',
        icon: 'cloud_download'
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
export function convertKey(key) {
  if (key === 'Locus_tag') {
    return 'Locus tag'
  } else if (key === 'Gene') {
    return 'Gene symbol'
  } else if (key === 'Old_locus_tag') {
    return 'Old locus tag'
  } else if (key === 'Chr') {
    return 'Chromosome'
  } else if (key === 'Type') return 'Gene type'
  else if (key === 'Protein_id') return 'Protein ID'
  else if (key === 'ref_seq_no') return 'Refseq Accession no. of genome'
  else if (key === 'latin_name') return 'Species'
  else {
    return key
  }
}

export function convertCyanoKey(key) {
  if (key === 'RefSeq_assm_no') return 'RefSeq Accession no.'
  else if (key === 'Tax_id') return 'Taxonomy ID'
  else if (key === 'Assembly_level') return 'Assembly level'
  else if (key === 'Assembly_name') return 'Assembly name'
  else if (key === 'Submission_date') return 'Submission date'
  else if (key === 'GenBank_assm_acc') return 'GenBank Accession no'
  else if (key === 'Submitter') return 'Submitter'
  else if (key === 'Chr_nos') return 'Numbers of chromosome'
  else if (key === 'Seq_len') return 'Total genomic sequence length'
  else if (key === 'Total_gene_no') return 'Total gene numbers'
  else if (key === 'Protein_coding') return 'Numbers of protein encoding genes'
  else if (key === 'Non-coding') return 'Numbers of non-coding genes'
  else if (key === 'Pseudo') return 'Numbers of  pseudogenes'
  else return key



}








