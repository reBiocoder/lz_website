<template>
  <div class="q-pa-md">
    <q-table
      :data="data"
      :columns="columns"
      :separator="separator"
      :pagination.sync="pagination"
      :rows-per-page-options="[50, 200, 500, 1000, 0]"
      :loading="loading"
      :filter="filter"
    >
      <template v-slot:top-left>
        <div class="text-h6">The keyword: <span class="text-orange text-italic">{{ keywords }}</span>
          <span class="text-purple" style="margin-left: 10px; font-size: 14px;">(RefSeq Accession no. or Locus_tag or Old_locus_tag or Gene or Product)</span>
        </div>
      </template>
      <template v-slot:top-right>
        <q-input borderless dense debounce="300" color="primary" v-model="filter"
                 label="Search data of current species">
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
            <q-tooltip>
              Some text as content of Tooltip
            </q-tooltip>
          </q-th>
        </q-tr>
      </template>
      <template v-slot:body-cell-Locus_tag="props">
        <q-td :props="props">
          <div>
            <router-link style="text-decoration: none;"
                         :to="{name: 'cyano_detail', params: {code: props.row.Locus_tag}}">
              {{ props.row.Locus_tag }}
            </router-link>
          </div>
        </q-td>
      </template>
      <template v-slot:body-cell-Gene="props">
        <q-td :props="props">
          <div>
            <router-link style="text-decoration: none;"
                         :to="{name: 'cyano_detail', params: {code: props.row.Gene}}">
              {{ props.row.Gene }}
            </router-link>
          </div>
        </q-td>
      </template>
      <template v-slot:body-cell-Old_locus_tag="props">
        <q-td :props="props">
          <div>
            <router-link style="text-decoration: none;"
                         :to="{name: 'cyano_detail', params: {code: props.row.Old_locus_tag}}">
              {{ props.row.Old_locus_tag }}
            </router-link>
          </div>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
import http from "src/api/display";
import {convertKey} from "src/utils/constants";

export default {
  name: "search_all",
  data() {
    return {
      keywords: "",
      filter: null,
      loading: true,
      pagination: {
        page: 1, //初始页面在1页
        rowsPerPage: 50 // 0 means all rows
      },
      separator: 'horizontal',
      columns: [],
      data: [],
    }
  },
  mounted: function () {
    this.keywords = this.$route.query["q"]  //得到查询内容
    http.global_search({"q": this.$route.query['q'], "type": "global"},
      (res) => {
        if (res.data.code === "success") {
          let header = res.data.data.header
          let raw_header = []
          for (let i = 0, len = header.length; i < len; ++i) {
            raw_header.push({
              "name": header[i],
              "label": convertKey(header[i]),
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
        this.loading = false
      }
    )
  }
}
</script>

<style scoped>

</style>
