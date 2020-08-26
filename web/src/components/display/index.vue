<template>
  <div>
    <div class="q-pa-md">
      <q-table
        :data="data"
        :columns="columns"
        :separator="separator"
        :pagination.sync="pagination"
        :rows-per-page-options="[50, 200, 500, 1000, 0]"
        :filter="filter"
      >
        <template v-slot:top-left>
          <div class="text-purple text-h6">626 complete or draft genomic data of cyanobacteria are included!</div>
        </template>
        <template v-slot:top-right>
          <q-input borderless dense debounce="300" color="primary" v-model="filter" label="Search for expect species">
            <template v-slot:append>
              <q-icon name="search"/>
            </template>
          </q-input>
        </template>
        <template v-slot:header="props">
          <q-tr :props="props">
            <q-th
              v-for="col in props.cols"
              :key="col.name"
              :props="props"
            >
              {{ col.label }}
<!--              <q-tooltip>-->
<!--                Some text as content of Tooltip-->
<!--              </q-tooltip>-->
            </q-th>
          </q-tr>
        </template>
        <template v-slot:body-cell-RefSeq_assm_no="props">
          <q-td :props="props">
            <div>
              <router-link style="text-decoration: none;"
                           :to="{name: 'cyano', params: {code: props.row.RefSeq_assm_no}}">
                {{props.row.RefSeq_assm_no}}
              </router-link>
            </div>
          </q-td>
        </template>
      </q-table>
    </div>
  </div>
</template>

<script>
  import http from '../../api/display'
  import { convertCyanoKey } from '../../utils/constants'

  export default {
    name: 'index',
    data() {
      return {
        filter: null,
        pagination: {
          page: 1, //初始页面在1页
          rowsPerPage: 50 // 0 means all rows
        },
        separator: 'horizontal',
        columns: [],
        data: [],
      }
    },
    method: {},
    components: {
    },
    mounted: function () {
      http.get_cyano_genomes((res) => {
          if (res.data.code === "success") {
            let header = res.data.data.header
            let raw_header = []
            for (let i = 0, len = header.length; i < len; ++i) {
              raw_header.push({
                "name": header[i],
                "label": convertCyanoKey(header[i]),
                "align": "center",
                "field": header[i],
                "sortable": true
              })
            }
            this.columns = raw_header
            this.data = res.data.data.data
          } else {
            this.$q.notify({
              message: res.data.info
            })
          }
        }
      )
    }
  }
</script>

<style scoped>

</style>
