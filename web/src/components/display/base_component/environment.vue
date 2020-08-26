<template>
  <div>
    <div class="q-pa-md shadow-0">
      <q-table
        :title="code"
        :data="data"
        :columns="columns"
        row-key="condition"
        separator="cell"
        :pagination.sync="pagination"
        card-class="shadow-0"
      >
        <template v-slot:body-cell-GSE="props">
          <q-td :props="props">
            <div>
              <span class="text-primary" @click="targetTo(props.row.GSE)">
                {{props.row.GSE}}
              </span>
            </div>
          </q-td>
        </template>
        <template v-slot:body-cell-condition="props">
          <q-td :props="props">
            <q-badge color="purple">
              {{ props.value }}
            </q-badge>
          </q-td>
        </template>
      </q-table>
    </div>
    <!--    <div class="q-pa-md">-->
    <!--      <q-tab-panel class="shadow-4">-->
    <!--        <div class="text-h6">{{`Difference analysis of ${this.$route.params.code}`}}</div>-->
    <!--        <q-separator/>-->
    <!--        <q-img style="width: 80%; height: 80%" :src="img_url"/>-->
    <!--      </q-tab-panel>-->
    <!--    </div>-->
  </div>
</template>

<script>
  import http from '../../../api/display'

  export default {
    name: "environment",
    data() {
      return {
        img_url: null,  //图片的url
        pagination: {
          page: 1, //初始页面在1页
          rowsPerPage: 0 // 0 means all rows
        },
        code: null,
        columns: [
          {
            name: 'GSE',
            field: 'GSE',
            align: 'center',
            label: 'GSE no.',
            sortable: true
          },
          {
            name: 'condition',
            field: 'condition',
            align: 'center',
            label: 'Conditions',
            sortable: true
          },
          {
            name: "log2FC",
            field: 'log2FC',
            align: 'center',
            label: 'Log2FolderChange',
            sortable: true,
          },
          {
            name: 'padj',
            field: 'padj',
            align: 'center',
            label: 'Adjusted p-value',
            sortable: true,
          },
        ],
        data: []
      }
    },
    props: ['locus_tag'],
    methods: {
      targetTo(code) {
        window.location.href = `https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=${code}`
      }
    },
    watch: {
      locus_tag: {
        handler(newVal, oldVal) {
          console.log("-------")
          console.log(newVal)

          this.code = `Controlled experiment with ${newVal}`
          http.search_environment({"q": newVal}, (res) => {
            if (res.data.code === "success") {
              if (res.data.data === []) {
                this.$q.notify({
                  message: "Please Refresh!"
                })
              } else {
                this.data = res.data.data
              }
            } else {
              this.$q.notify({
                message: "Error! Try again"
              })
            }
          })
        }
      }
    },
    created() {
      this.code = `Controlled experiment with ${this.locus_tag}`
      http.search_environment({"q": this.locus_tag}, (res) => {
        if (res.data.code === "success") {
          if (res.data.data === []) {
            this.$q.notify({
              message: "Please Refresh!"
            })
          } else {
            this.data = res.data.data
          }
        } else {
          this.$q.notify({
            message: "Error! Try again"
          })
        }
      })
    },
    // //得到图片
    // http.environment_image({"q": this.$route.params.code}, (res) => {
    //   if (res.data.code === 'success') {
    //     this.img_url = res.data.data.img_url
    //   } else {
    //     this.$q.notify({
    //       message: 'Error! Try again'
    //     })
    //   }
    // })

  }
</script>

<style scoped>

</style>
