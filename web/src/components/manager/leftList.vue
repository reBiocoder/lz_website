<template>
  <div>
    <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
      <div class="absolute-bottom bg-transparent">
        <q-avatar size="56px" class="q-mb-sm">
          <img src="https://cdn.quasar.dev/img/boy-avatar.png">
        </q-avatar>
        <div class="text-weight-bold">{{this.state_real_name}}</div>
        <div>{{this.state_username}}</div>
      </div>
    </q-img>
    <q-tree
      :nodes="main_menu"
      node-key="code"
      style="margin-top: 150px;font-size: 16px"
      :no-nodes-label="$t('message.noData', 'zh-hans')"
      :expanded.sync="expand"
    >
      <div class="cursor-pointer" slot="default-header" slot-scope="prop" @click.stop="selectedNode(prop.node)">
        {{ prop.node.name }}
      </div>
    </q-tree>

  </div>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    data() {
      return {
        username: null,
        expand: [],
        main_menu: [
          {
            code: 'drgn',
            name: '导入功能',
            children: [
              {code: 'csv', name: '导入csv表格'},
              {code: 'excel', name: '导入excel表格'}
            ]
          },
          {
            code: 'manager',
            name: '管理表格'
          }
        ]
      }
    },
    computed: {
      ...mapState(process.env.APP_SCOPE_NAME, {
      "state_username": 'username',
      "state_real_name": 'real_name'
    })
    },
    methods: {
      selectedNode(node) {
        console.log(node)
      },
      changeRouter(code) {
        this.$router.push({
          name: 'content',
          params: {
            username: this.username,
            code: code
          }
        })
      },
    }
  }
</script>

<style scoped>

</style>
