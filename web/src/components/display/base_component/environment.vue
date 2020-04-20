<template>
  <div>
    <div class="q-pa-md">
      <q-table
        class="shadow-0"
        :title="code"
        :data="data"
        :columns="columns"
        row-key="condition"
        separator="cell"
        :pagination.sync="pagination"
      >
        <template v-slot:body-cell-condition="props">
          <q-td :props="props">
            <q-badge color="purple">
              {{ props.value }}
            </q-badge>
          </q-td>
        </template>
      </q-table>
    </div>
    <div class="q-pa-md">
        <q-tab-panel   name="picture" class="shadow-0">
          <div class="text-h6">{{`Volcano plot of ${this.$route.params.code}`}}</div>
            <q-separator />
          <q-img style="width: 80%; height: 80%" :src="img_url"/>
        </q-tab-panel>
    </div>
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
          rowsPerPage: 10 // 0 means all rows
        },
        code: null,
        columns: [
          {
            name: 'condition',
            field: 'condition',
            align: 'center',
            label: 'condition',
            sortable: true
          },
          {
            name: 'padj',
            field: 'padj',
            align: 'center',
            label: 'padj',
            sortable: true,
          },
          {
            name: "log2",
            field: 'log2',
            align: 'center',
            label: 'log2FoldChange',
            sortable: true,
          }
        ],
        data: []
      }
    },
    mounted() {
      this.code = `Differential analysis of ${this.$route.params.code}`
      http.search_environment({"q": this.$route.params.code}, (res) => {
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

      //得到图片
      http.environment_image({"q": this.$route.params.code}, (res) => {
        if(res.data.code === 'success'){
          this.img_url = res.data.data.img_url
        }
        else{
          this.$q.notify({
            message: 'Error! Try again'
          })
        }
      })
    }
  }
</script>

<style scoped>

</style>
