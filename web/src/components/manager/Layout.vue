<template>
  <q-layout view="lhh lpr fff">

    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
<!--        <q-btn dense flat round icon="menu" @click="left = !left"/>-->

        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo/svg/quasar-logo.svg">
          </q-avatar>
          主菜单
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <leftList></leftList>

    <q-page-container>
      <router-view/>
    </q-page-container>

  </q-layout>
</template>

<script>
  import leftList from "./leftList";

  export default {
    data() {
      return {
        left: false
      }
    },
    components: {
      leftList
    }
  }
</script>
