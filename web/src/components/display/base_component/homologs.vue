<template>
  <div>
    <div class="q-pa-md shadow-0">
      <q-table
        :data="data"
        :columns="columns"
        row-key="Locus_tag"
        separator="cell"
        :pagination.sync="pagination"
        card-class="shadow-0"
      >
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
      </q-table>
    </div>
    <q-inner-loading :showing="visible" >
      <q-spinner-gears size="50px" color="primary"/>
      <p class="text-purple text-body1">The blastP is running in the background, please be patient!</p>
    </q-inner-loading>
  </div>
</template>

<script>
  import http from '../../../api/display'

  export default {
    name: "homologs",
    data() {
      return {
        pagination: {
          page: 1, //初始页面在1页
          rowsPerPage: 50 // 0 means all rows
        },
        columns: [
          {
            name: 'Locus_tag',
            field: 'Locus_tag',
            align: 'center',
            label: 'Locus tag',
            sortable: true
          },
          {
            name: 'Identity',
            field: 'Identity',
            align: 'center',
            label: 'Identity (%)',
            sortable: true
          },
          {
            name: "Coverage",
            field: 'Coverage',
            align: 'center',
            label: 'Coverage (%)',
            sortable: true,
          },
          {
            name: 'E-Value',
            field: 'E-Value',
            align: 'center',
            label: 'E-Value',
            sortable: true,
          },
          {
            name: 'Protein_ID',
            field: 'Protein_ID',
            align: 'center',
            label: 'Protein_ID',
            sortable: true,
          },
          {
            name: 'Product',
            field: 'Product',
            align: 'center',
            label: 'Product',
            sortable: true,
          },
          {
            name: 'Species',
            field: 'Species',
            align: 'center',
            label: 'Species',
            sortable: true,
          },
        ],
        data: [],
        visible: true,
      }
    },
    props: ['locus_tag'],
    mounted() {
      http.get_homolog({"locus_tag": this.locus_tag}, (res) => {
        if (res.data.code === "success") {
          if (res.data.data.data === []) {
            this.$q.notify({
              message: "Please Refresh!"
            })
          } else {
            this.data = res.data.data.data
          }
        } else {
          this.$q.notify({
            message: "Error! Try again"
          })
        }
        this.visible = false
      })
    },
  }
</script>

<style scoped>

</style>
