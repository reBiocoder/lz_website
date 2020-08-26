<template>
  <div class="q-pa-md">
    <q-table
      no-data-label="Not Found Data"
      title="Search Result"
      :data="data"
      :columns="columns"
      row-key="Locus_tags"
      :separator="separator"
    >
      <template v-slot:body-cell-Locus_tags="props">
        <q-td :props="props">
          <div>
            <router-link :to="{name: 'detail', params: {code: props.row.Locus_tags}}">
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
  import {mapState} from 'vuex'

  export default {
    name: 'search',
    data() {
      return {
        separator: 'horizontal',
        columns: [],
        data: [],
      }
    },
    computed: {
      ...mapState(process.env.APP_SCOPE_NAME, ["search_content"])
    },
    method: {},
    mounted: function () {
      http.index_random_col((res) => {
        if (res.data.code === "success") {
          console.log(res.data.data)
          this.columns = res.data.data
        }
      })
      http.search_data({"q": this.$route.params.code}, (res) => {
        if (res.data.code === 'success') {
          this.data = res.data.data
        } else {
          this.$q.notify({
            message: "Not Found Result"
          })
        }
      })
    }
  }
</script>

<style scoped>

</style>
