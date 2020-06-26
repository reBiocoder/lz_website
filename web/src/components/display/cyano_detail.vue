<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md">
      <q-tab-panels v-model="panel" animated class="shadow-2 rounded-borders">
        <q-tab-panel name="locus_tag">
          <div class="text-h5">{{this.code}}</div>
          <q-badge v-for="i in this.label" color="purple" style="margin-right: 10px;">{{i}}</q-badge>
          <div class="messageBlock">
            <div class="messageBox1">
              <p v-for="i in this.data1">
                <span v-for="(j, z) in i" class="messageLabel ng-binding">{{z}}: <span
                  style="font-weight: 350;margin-left: 10px;">{{j}}</span></span>
              </p>
            </div>
            <div class="messageBox2">
              <p v-for="i in this.data2">
                <span v-for="(j, z) in i" class="messageLabel ng-binding">{{z}}:  <span
                  style="font-weight: 350;margin-left: 10px;">{{j}}</span></span>
              </p>
            </div>
          </div>
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
          <q-tab name="environment" label="GENE EXPRESSION"/>
          <q-tab name="jbrowse" label="JBrowse"/>
          <q-tab name="references" label="references"/>
          <q-tab name="sequences" label="sequences"/>
          <q-tab name="homologs" label="homologs"/>
          <q-tab name="mutants" label="mutants"/>

        </q-tabs>

        <q-separator/>

        <q-tab-panels v-model="tab" animated>

          <q-tab-panel name="environment">
            <environment></environment>
          </q-tab-panel>

          <q-tab-panel name="jbrowse">
            <jbrowse></jbrowse>
          </q-tab-panel>

          <q-tab-panel name="references">
            <references></references>
          </q-tab-panel>

          <q-tab-panel name="sequences">
            <sequences></sequences>
          </q-tab-panel>

          <q-tab-panel name="homologs">
            <homologs></homologs>
          </q-tab-panel>

          <q-tab-panel name="mutants">
            <mutants></mutants>
          </q-tab-panel>
        </q-tab-panels>
      </q-card>
    </div>
  </div>
</template>

<script>
  import http from '../../api/display'
  import environment from "./base_component/environment";
  import jbrowse from "./base_component/jbrowse"
  import references from "components/display/base_component/references";
  import sequences from "components/display/base_component/sequences";
  import homologs from "components/display/base_component/homologs";
  import mutants from "components/display/base_component/mutants";

  export default {
    name: "cyano_detail",
    data() {
      return {
        tab: 'environment',
        code: "",
        panel: 'locus_tag',
        data1: null,
        data2: null,
        label: null,
      }
    },
    mounted() {
      this.$q.loading.show({
        message:"Some important <b>process</b> is in progress..."
      })
      http.search_detail({"mg_type": "display", "q": this.$route.params.code}, (res) => {
        this.code = res.data.data.locus_tag
        this.data1 = res.data.data.data1
        this.data2 = res.data.data.data2
        this.label = res.data.data.label
        this.$q.loading.hide()
      })
    },
    components: {
      environment, jbrowse, references, sequences, homologs, mutants
    }
  }
</script>

<style scoped>
  .messageBlock {
    display: table;
    width: 100%;
    margin-top: 5px;
    padding: 20px;
    background-color: #ffffff;
  }

  .messageBlock .messageBox1 {
    display: table-cell;
    width: 50%;
  }

  .messageBlock .messageBox2 {
    display: table-cell;
    width: 50%;
  }

  .messageBlock .messageBox3 {
    display: table-cell;
    width: 10%;
    padding-left: 20px;
    border-left: 1px solid #ddd;
  }

  .messageBlock .messageLabel {
    font-size: 14px;
    font-weight: 500;
    margin-right: 10px;
  }

  .messageBlock .messageImage {
    width: 20px;
  }

  .messageTitle {
    margin: 10px 0;
  }

</style>
