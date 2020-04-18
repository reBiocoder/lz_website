<template>
  <div>
    <div class="q-pa-md">
      <q-uploader
        ref="abort"
        style="width: auto"
        @start="uploading_csv"
        @added="add_csv"
        @uploaded="uploaded"
        field-name="csv_data"
        :url=url
        :form-fields="[{name:'table',value: table1}]"
      >
        <template v-slot:header="scope">
          <div class="row no-wrap items-center q-pa-sm q-gutter-xs">
            <q-btn v-if="scope.queuedFiles.length > 0" icon="clear_all" @click="scope.removeQueuedFiles" round dense
                   flat>
              <q-tooltip>清楚所有文件</q-tooltip>
            </q-btn>
            <q-btn v-if="scope.uploadedFiles.length > 0" icon="done_all" @click="scope.removeUploadedFiles" round dense
                   flat>
              <q-tooltip>移除上传文件</q-tooltip>
            </q-btn>
            <q-spinner v-if="scope.isUploading" class="q-uploader__spinner"/>
            <div class="col-1">
              <div class="q-uploader__title">请上传csv文件</div>
              <div class="q-uploader__subtitle">{{ scope.uploadSizeLabel }} / {{ scope.uploadProgressLabel }}</div>
            </div>
            <div class="col">
              <div class="q-gutter-sm" v-if="is_visibled">
                <span class="text-left fit q-pt-md">请选择想要上传到的表：</span>
                <q-radio keep-color v-model="table1" val="tss" label="tss" color="white"/>
                <q-radio keep-color v-model="table1" val="gen_exp" label="gen_exp" color="white"/>
                <q-radio keep-color v-model="table1" val="utex" label="utex" color="white"/>
              </div>
            </div>
            <q-btn v-if="scope.canAddFiles" type="a" icon="add_box" round dense flat>
              <q-uploader-add-trigger/>
              <q-tooltip>选择文件</q-tooltip>
            </q-btn>
            <q-btn v-if="scope.canUpload" icon="cloud_upload" @click="scope.upload" round dense flat>
              <q-tooltip>点击上传</q-tooltip>
            </q-btn>

            <q-btn v-if="scope.isUploading" icon="clear" @click="scope.abort" round dense flat>
              <q-tooltip>放弃上传</q-tooltip>
            </q-btn>
          </div>
        </template>
      </q-uploader>
    </div>
    <div class="q-pa-md" v-if="is_coled">
      <q-card>
        <q-card-section>
          <div class="text-h6">{{this.table1}}的表头</div>
          <div>
            <table class="text-justify" border="0" cellpadding="10" cellspacing="0">
              <tr>
                <th v-for="i in this.col" style="border: 1px solid #f00">{{ i }}</th>
              </tr>
            </table>
            <br>
            <p class="text-blue">请注意！ 上传的csv文件的表头需要与上传表格的表头一致，否则会造成一些错误！</p>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
  import http from '../../../api/backStage'
  import {QSpinnerFacebook} from 'quasar'

  export default {
    name: "csv",
    data() {
      return {
        is_coled:false, //表头信息不展示
        col:null,
        url: '/api/upload_csv/',
        table1: null,
        is_visibled: false, // 是否显示table
      }
    },
    methods: {
      uploading_csv() { //开始上传文件时
        if (this.table1 === null) {
          this.$q.notify({
            message: "请选择需要上传的表格"
          })
          this.$refs.abort.abort()  //终止上传文件
        }
      },
      add_csv(files) {//当在列表中添加文件时
        this.is_visibled = true
      },
      uploaded(info) { //当文件上传成功之后
        let res = JSON.parse(info.xhr.response)
        if (res.code === 'success') {
          this.$q.notify({
            message: res.info,
            color: 'purple',
            position: 'bottom',
            icon: 'done'
          })
          this.$refs.abort.reset()  //复位上传文件工具
          this.is_visibled = false // 隐藏表格信息
        } else {
          this.$q.notify({
            message: res.info,
          })
        }
      }
    },
    watch: {
      table1(newVal, oldVal) {
        const spinner = typeof QSpinnerFacebook !== 'undefined'
          ? QSpinnerFacebook // Non-UMD, imported above
          : Quasar.components.QSpinnerFacebook // eslint-disable-line
        this.$q.loading.show({
          spinner,
          spinnerColor: 'purple',
          spinnerSize: 140,
          message: "正在处理请求，获取表头中..."
        })
        http.getColKeys({'col_name': newVal}, (res) => {
          this.$q.loading.hide() //得到结果，隐藏ng
          this.col = res.data.data.col_keys
          this.is_coled = true
          console.log(res.data)
        })

      }
    }

  }
</script>

<style scoped>

</style>
