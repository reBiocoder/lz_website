<template>
  <div class="q-pa-md">
    <q-table
      title="Treats"
      :data="data"
      :columns="columns"
      row-key="name"
      :separator="separator"
    />
  </div>
</template>

<script>
  export default {
    name: 'database',
    data() {
      return {
        separator: 'cell',
        columns: [

        ],
        data: []
      }
    }
  }
</script>

<style scoped>

</style>
