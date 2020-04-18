<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md">
      <q-tab-panels v-model="panel" animated class="shadow-2 rounded-borders">
        <q-tab-panel name="locus_tag">
          <div class="text-h5">{{this.$route.params.code}}</div>
          <q-badge color="purple">Cyanobacteria</q-badge>
        </q-tab-panel>
      </q-tab-panels>
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          class="text-grey"
          active-color="primary"
          indicator-color="primary"
          align="justify"
          narrow-indicator
        >
          <q-tab name="base" label="Base Information"/>
          <q-tab name="environment" label="Environment"/>
          <q-tab name="jbrowse" label="JBrowse"/>
        </q-tabs>

        <q-separator/>

        <q-tab-panels v-model="tab" animated>
          <q-tab-panel name="base">
            <base-data></base-data>
          </q-tab-panel>

          <q-tab-panel name="environment">
            <environment></environment>
          </q-tab-panel>

          <q-tab-panel name="jbrowse">
            <jbrowse></jbrowse>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>

<script>
  import http from '../../api/display'
  import base_data from "./base_component/base"
  import environment from "./base_component/environment";
  import jbrowse  from "./base_component/jbrowse"
  export default {
    name: "detail",
    data() {
      return {
        tab: 'base',
        panel: 'locus_tag',
      }
    },
    components: {
      "base-data": base_data,
      environment,
      jbrowse
    }
  }
</script>

<style scoped>

</style>
