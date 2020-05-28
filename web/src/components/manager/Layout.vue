<template>
  <q-layout view="lHh lpR fFf">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-btn dense flat round icon="menu" @click="left = !left"/>

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          {{ this.click_title }}
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="left" side="left" content-class="bg-blue-grey-2" :width="230">
      <!-- drawer content -->
      <mgAside></mgAside>
    </q-drawer>

    <q-page-container>
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
  import mgAside from "components/manager/mgAside";
  import {mapState} from 'vuex';

  export default {
    data() {
      return {
        left: true
      }
    },
    computed: {
      ...mapState(process.env.APP_SCOPE_NAME, ['click_title']),
    },
    components: {
      mgAside
    },
  }
</script>
