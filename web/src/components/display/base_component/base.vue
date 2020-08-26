<template>
  <div class="q-pa-md">
    <q-table
      :title="code"
      :data="data"
      :columns="columns"
      row-key="key"
      separator="cell"
      :rows-per-page-options="[0]"
      :pagination.sync="pagination"
      :hide-header=true
      :hide-bottom=true
    >
      <template v-slot:body-cell-key="props">
        <q-td :props="props" :auto-width=false style="width: 20%;background-color: rgb(109, 81, 136);">
          {{props.value}}
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
  import http from '../../../api/display'
  import {mapMutations} from 'vuex'
  export default {
    name: "base_data",
    data() {
      return {
        pagination: {
          page: 1,
          rowsPerPage: 0 // 0 means all rows
        },
        code: 'Detail',
        columns: [
          {name: 'key', label: 'key', field: "key", align: 'center'},
          {name: 'value', label: 'value', field: "value", align: 'center'}
        ],
        data: []
      }
    },
    methods:{
      ...mapMutations(process.env.APP_SCOPE_NAME, ['changeGeneStart','changeGeneEnd'])
    },
    mounted() {
      this.code = `Base Information Of ${this.$route.params.code}`
      http.search_detail({"q": this.$route.params.code}, (res) => {
        if (res.data.code === "success") {
          this.data = res.data.data
          console.log(this.data)
          //从数组中得到该基因的起始位点和终止位点
          for(let j=0, len=this.data.length; j< len; ++j ){
            if(this.data[j].key === 'Start'){
              this.changeGeneStart(this.data[j].value)
            }
            if(this.data[j].key === 'End'){
              this.changeGeneEnd(this.data[j].value)
            }
          }
        //成功得到起始位点和终止位点
        } else {
          this.$q.notify({
              message: "Please try again"
            }
          )
        }
      })
    }
  }
</script>

<style scoped>

</style>
