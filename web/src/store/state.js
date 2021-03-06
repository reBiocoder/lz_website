let state = {
  // 前端展示所需要的信息
  requestBody: null,
  username: null,
  real_name: null,
  search_content: null,
  gene_start:null,
  gene_end:null,
  locus_tag: null, //locus_tag
  dna_sequence: '', //下载DNA序列
  protein_sequence: '', //下载蛋白质序列
  default_sequence: '',  //点击sequence返回最初的值

  //后台管理所需要的数据
  click_title: "", //当前侧边栏所点击的栏目
}
export default state
