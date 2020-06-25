<template>
  <div class="q-pa-md">
    <q-card>
      <q-tab-panel name="base_data" class="shadow-0">
        <div class="row">
          <div class="col-md-1 text-subtitle2" style="padding-top: 5px;">
            <q-icon name="keyboard_backspace"/>
            返回
          </div>
          <q-separator vertical inset/>
          <div class="col-md-3 text-primary text-h6">配置M744_RS13850</div>
        </div>
        <q-separator/>
        <!--修改表单---------------->
        <div class="row">
          <q-form
            @submit="onSubmit"
            @reset="onReset"
            class="q-gutter-md q-pt-md col-8"
          >
            <div class="row" :key="i" v-for="(each_data, i) in this.data">
              <div class="col-2">{{each_data.key}}</div>
              <q-input v-if="each_data.const_key == 'locus_tags'" disable :ref="each_data.const_key" class="col-10"
                       outlined v-model="each_data.value"
                       :name="each_data.key" type="text" :dense="true">
              </q-input>
              <q-input v-else :ref="each_data.const_key" class="col-10" outlined v-model="each_data.value"
                       :name="each_data.key" type="text" :dense="true">
              </q-input>
            </div>
            <div>
              <q-btn label="确认修改" type="submit" color="primary"/>
              <q-btn label="删除数据" type="reset" color="deep-orange" class="q-ml-sm"/>
            </div>
          </q-form>
          <div class="col-4">
            <div class="q-px-lg q-pb-md">
              <q-timeline  >
                <q-timeline-entry heading tag="h7">
                  历史记录
                </q-timeline-entry>

                <q-timeline-entry
                  title="Event Title"
                  subtitle="February 22, 1986"
                  body="123"
                >
                </q-timeline-entry>

                <q-timeline-entry
                  title="Event Title"
                  subtitle="February 21, 1986"
                  icon="delete"
                  body="456"
                >
                </q-timeline-entry>

              </q-timeline>
            </div>

          </div>
        </div>

      </q-tab-panel>
    </q-card>
  </div>
</template>

<script>
  import http from '../../../api/display'
  import back_http from '../../../api/backStage'

  export default {
    name: "baseDataChange",
    data() {
      return {
        data: null,
      }
    },
    methods: {
      onSubmit() { //确认提交数据
        console.log(this.$refs)
        let res = {}
        let document = {}
        for (let i in this.$refs) {
          if (i === 'locus_tags') {
            res["primary_key"] = this.$refs[i][0].value
            document[this.$refs[i][0].name] = this.$refs[i][0].value
          } else {
            document[this.$refs[i][0].name] = this.$refs[i][0].value
          }
        }
        res["document"] = document
        back_http.update_utex_tss_data(res, (resu) => {
          console.log(resu)
        })
      },
      onReset() {

      }
    },
    mounted() {
      http.search_detail({"q": this.$route.params.code, 'mg_type': 'manager'}, (res) => {
        if (res.data.code === "success") {
          this.data = res.data.data
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
