<template>
  <div>
    expression
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
        columns: [],
        data: []
      }
    },
    mounted() {

    }
  }
</script>

<style scoped>

</style>
