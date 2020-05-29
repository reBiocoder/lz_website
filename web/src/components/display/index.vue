<template>
  <div class="q-pa-md">
    <q-table
      title="Cyanobacteria Database "
      :data="data"
      :columns="columns"
      row-key="Locus_tags"
      :separator="separator"
      :pagination.sync="pagination"
    >
      <template v-slot:body-cell-Locus_tags="props">
        <q-td :props="props">
          <div>
            <router-link  style="text-decoration: none;" :to="{name: 'detail', params: {code: props.row.Locus_tags}}">
              {{props.row.Locus_tags}}
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
          rowsPerPage: 10 // 0 means all rows
        },
        separator: 'cell',
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
