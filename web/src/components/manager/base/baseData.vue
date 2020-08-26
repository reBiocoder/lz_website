<template>
  <div class="q-pa-md">
    <q-card>
      <q-tab-panel name="base_data" class="shadow-0">
        <div class="text-h6 text-primary row">
          <div class="col-md-2" style="padding-top: 5px;">
            基础数据配置
          </div>
          <div class="col-3">
            <q-input outlined label="输入locus_tag进行配置" v-model="search_data" style="margin-bottom: 10px;" :dense="true">
              <template v-slot:append>
                <q-icon name="search"/>
              </template>
            </q-input>
          </div>
        </div>
        <q-separator/>

        <q-table
          :data="data"
          :columns="columns"
          row-key="Locus_tags"
          :separator="separator"
          :pagination.sync="pagination"
          class="shadow-0"
        >
          <template v-slot:body-cell-Locus_tags="props">
            <q-td :props="props">
              <div>
                <router-link style="text-decoration: none;" :to="{name: 'manager_baseDataChange', params: {code: props.row.Locus_tags}}">
                  {{props.row.Locus_tags}}
                </router-link>
              </div>
            </q-td>
          </template>
        </q-table>

      </q-tab-panel>
    </q-card>
  </div>
</template>

<script>
  import http from "src/api/display";

  export default {
    name: "baseData",
    data() {
      return {
        search_data: "",
        pagination: {
          page: 1, //初始页面在1页
          rowsPerPage: 20 // 0 means all rows
        },
        separator: 'horizontal',
        columns: [],
        data: [],
      }
    },
    method: {},
    mounted: function () {
      http.index_random_col((res) => {
        if (res.data.code === "success") {
          this.columns = res.data.data
        }
      })
      http.index_random_data((res) => {
        if (res.data.code === 'success') {
          this.data = res.data.data
        }
      })
    }
  }
</script>

<style scoped>

</style>
