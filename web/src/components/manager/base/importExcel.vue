<template>
  <div>
    <div class="q-pa-md">
      <div class="q-card">
        <q-tab-panel name="mails">
          <div class="row">
            <div class="text-h6 col-8">
              <div class="row">
                <div class="col-5">当前选择的表格为：{{ table_title}}</div>
                <div class="col-3">
                  <q-select @input="selectTable" outlined v-model="model" :options="options" label="请选择导入表格"
                            style="height: 30px;" dense/>
                </div>
                <div class="col-4"></div>
              </div>
            </div>
            <div class="col-2">
              <input v-show="false" :ref="table_title" @change="getUploadFile" type="file"/>
              <q-btn color="black" @click.stop="triggerChangeFile(table_title)" label="导入">
              </q-btn>
            </div>
            <div class="col-2">
              <q-btn color="black" label="导出"/>
            </div>
          </div>
          <q-table
            class="q-mt-md"
            :data="data"
            :columns="columns"
            row-key="name"
            separator="cell"
            :no-data-label="table_title"
          >
            <template v-slot:no-data="{message}">
              <div class="text-left">
                以上是<span class="text-orange">{{ message }}</span>的表头部分，请严格按照表头的编码上传数据
              </div>
            </template>
          </q-table>
        </q-tab-panel>
      </div>
    </div>
  </div>
</template>

<script>
  import http from '../../../api/backStage.js'

  export default {
    name: "importExcel",
    data() {
      return {
        table_title: "",
        model: null,

        options: [
          'padj_log2', 'cyano_genomes','cyano_all_gff',
        ],

        panel: 'mails',
        separator: 'vertical',

        columns: [],

        data: []
      }
    },
    methods: {
      selectTable(value) {  // 选择不同的表格
        this.table_title = value
        http.getColKeys({"col_name": value}, (res) => {
          let header = []
          let res_list = res.data.data.col_keys
          for (let i = 0, len = res_list.length; i < len; ++i) {
            header.push({
              "name": res_list[i],
              "label": res_list[i],
              "align": "center",
              "field": res_list[i]
            })
          }
          this.columns = header
        })
      },
      triggerChangeFile(table_name) {
        this.$refs[table_name].click()
      },
      getUploadFile(event) { //上传文件接口
        let file = event.target.files[0]
        if (file) {
          let splits = file.name.split('.')
          let suffix = splits[splits.length - 1]
          if (suffix === 'tab' || suffix === "xlsx") {
            this.uploadFile(file, event)
          } else {
            //this.$refs.excelFile.value = ''
            this.$q.notify({
              message: "请选择格式为.tab的文件!"
            })
          }
        }
      },
      uploadFile(file, event) {
        this.$q.loading.show({
          message: '正在上传数据，请耐心等待...'
        })
        let formData = new FormData()
        formData.append('file', file)
        formData.append('table_name', this.table_title)
        http.uploadexcel(formData, res => {
          if (res.data.code === "success") {
            // 上传成功
            this.$q.notify({
              message: '数据上传成功！',
              color: 'positive'
            })
            this.$q.loading.hide()  //隐藏等待窗口
            event.target.value = "" //清空该值
          }
          else{
            this.$q.notify({
              message: '数据上传失败！',
              color: 'error'
            })
            this.$q.loading.hide()  //隐藏等待窗口
            event.target.value = "" //清空该值
          }
        })
      },
    }
  }
</script>

<style scoped>

</style>
