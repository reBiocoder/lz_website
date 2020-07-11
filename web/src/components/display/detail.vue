<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md">
      <q-tab-panels v-model="panel" animated class="shadow-2 rounded-borders">
        <q-tab-panel name="locus_tag">
          <div class="text-h5">{{this.code}}</div>
          <q-badge color="purple">Synechococcus elongatus UTEX2973</q-badge>
          <div class="messageBlock">
            <div class="messageBox1">
              <p v-for="i in this.data1">
                <span class="messageLabel ng-binding">{{i.key}}:</span>
                <span class="messageContent ng-binding">{{i.value}}</span>
              </p>
            </div>
            <div class="messageBox2">
              <p v-for="i in this.data2">
                <span class="messageLabel ng-binding">{{i.key}}:</span>
                <span class="messageContent ng-binding">{{i.value}}</span>
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

  import {mapMutations} from "vuex";

  const SCOPE = process.env.APP_SCOPE_NAME
  export default {
    name: "detail",
    data() {
      return {
        tab: 'environment',
        panel: 'locus_tag',
        data1: [],
        data2: [],
        code: null,
        name: null,
      }
    },
    methods: {
      ...mapMutations(SCOPE, ['changeGeneStart', 'changeGeneEnd', 'changeLocus_tag'])
    },
    mounted() {
      this.code = `Basic Information Of ${this.$route.params.code}`
      http.search_detail({"q": this.$route.params.code, 'mg_type': 'display'}, (res) => {
        if (res.data.code === "success") {
          this.data1 = res.data.data.data1
          this.data2 = res.data.data.data2
          this.changeGeneStart(res.data.data.start)
          this.changeGeneEnd(res.data.data.end)
          this.changeLocus_tag(res.data.data.locus_tag) //将当前正在检索的locus_tag存储在vuex中
        } else {
          this.$q.notify({
              message: "Please try again"
            }
          )
        }
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
