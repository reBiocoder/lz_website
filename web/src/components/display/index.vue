<template>
  <div class="q-pa-md">
    <q-table
      title="Cyanobacteria Database "
      :data="data"
      :columns="columns"
      row-key="Locus_tags"
      :separator="separator"
      :pagination.sync="pagination"
      :rows-per-page-options="[50, 100, 200, 500, 0]"
    >
      <template v-slot:body-cell-Species="props">
        <q-td :props="props">
          <div>
            <router-link style="text-decoration: none;" :to="{name: 'detail', params: {code: props.row.Species}}">
              {{props.row.Species}}
            </router-link>
          </div>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
  import http from '../../api/display'

  export default {
    name: 'index',
    data() {
      return {
        pagination: {
          page: 1, //初始页面在1页
          rowsPerPage: 50 // 0 means all rows
        },
        separator: 'cell',
        columns: [],
        data: [],
      }
    },
    method: {},
    mounted: function () {
      http.get_cyano_genomes((res) => {
          if (res.data.code === "success") {
            let header = res.data.data.header
            let raw_header = []
            for (let i = 0, len = header.length; i < len; ++i) {
              raw_header.push({
                "name": header[i],
                "label": header[i],
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
