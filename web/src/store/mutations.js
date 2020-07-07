export const updateRequestBody = (state, data) => {
  if (data) {
    state.requestBody = data
  }
}
export const real_name = (state, data) => {
  if(data){
    state.real_name = data
  }
}
export const username = (state, data) => {
  if(data){
    state.username = data
  }
}
export const changeSearchContent = (state, data) => {
  if(data){
    state.search_content = data
  }
}
export const changeGeneStart = (state, data) => {
  if(data){
    state.gene_start = data
  }
}
export const changeGeneEnd = (state, data) => {
  if(data){
    state.gene_end = data
  }
}

export const changeClickTitle = (state, data) => {
  if(data){
    state.click_title = data
  }
}

export const changeLocus_tag = (state, data) => { //存储当前搜索的locus_tag
  if(data){
    state.locus_tag = data
  }
}
