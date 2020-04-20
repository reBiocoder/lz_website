<template>
    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      :width="240"
    >
      <q-scroll-area class="fit">
            <q-img class="absolute-top" src="https://cdn.quasar.dev/img/material.png" style="height: 150px">
      <div class="absolute-bottom bg-transparent">
        <q-avatar size="56px" class="q-mb-sm">
          <img src="https://cdn.quasar.dev/img/boy-avatar.png">
        </q-avatar>
        <div class="text-weight-bold"></div>
        <div></div>
      </div>
    </q-img>
        <q-list padding style="margin-top: 150px;">
          <q-item v-for="link in links1" :key="link.text" @click="func(link.code)" v-ripple clickable>
            <q-item-section avatar>
              <q-icon color="grey" :name="link.icon"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ link.text }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>
    </q-drawer>
</template>

<script>
  import http from '../../api/backStage'
  export default {
    data() {
      return {
        leftDrawerOpen: false,

        links1: [],
      }
    },
    methods:{
      func(code){
        this.$router.push({"name": code})
      }
    },
    mounted() {
      http.initMenu((res)=>{
        this.links1 = res.data.data.result;
      })
    }
  }
</script>
<style scoped>

</style>
