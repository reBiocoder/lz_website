<template>
  <div class="q-pa-md">
    <div class="q-gutter-y-md">
      <q-tab-panels v-model="panel" animated class="shadow-2 rounded-borders">
        <q-tab-panel name="locus_tag">
          <div class="text-h5">{{ this.code }}</div>
          <q-badge v-for="(m, n) in this.label" color="purple" style="margin-right: 10px;" :key="n">{{ m }}</q-badge>
          <div class="messageBlock">
            <div class="messageBox1">
              <p v-for="i in this.data1">
                <span v-for="(j, z) in i" class="messageLabel ng-binding">{{ convertKey(z) }}: <span
                  style="font-weight: 350;margin-left: 10px;">{{ j }}</span></span>
              </p>
            </div>
            <div class="messageBox2">
              <p v-for="i in this.data2">
                <span v-for="(j, z) in i" class="messageLabel ng-binding">{{ convertKey(z) }}:  <span
                  style="font-weight: 350;margin-left: 10px;">{{ j }}</span></span>
              </p>
            </div>
          </div>
        </q-tab-panel>
      </q-tab-panels>
      <q-card>
        <q-tabs
          v-model="tab"
          dense
          align="justify"
          inline-label
          indicator-color="blue"
          active-bg-color="blue"
          active-color="black"
          class="bg-blue-14  text-white shadow-2"
        >
          <q-tab name="jbrowse" label="JBrowse"/>
          <q-tab @click="default_seq" name="sequences" label="sequences"/>
          <q-tab name="homologs" label="homologs"/>
          <q-tab name="references" label="references"/>
          <q-tab name="environment" label="GENE EXPRESSION"/>
          <q-tab name="mutants" label="mutants"/>

        </q-tabs>

        <q-separator/>

        <q-tab-panels v-model="tab" :keep-alive="isHomologed" animated>

          <q-tab-panel name="jbrowse">
            <jbrowse :ref_seq_no.sync="refSeqNo"
                     :start.sync="oldStart"
                     :end.sync="oldEnd"
                     :chr="oldChr">

            </jbrowse>
          </q-tab-panel>

          <q-tab-panel name="sequences">
            <sequences :ref_no.sync="refSeqNo"
                       :chr.sync="oldChr"
                       :strand.sync="oldStrand"
                       :Lstart.sync="oldStart"
                       :Lend.sync="oldEnd"
                       :locus_tag.sync="locus_tag"
                       :protein_id="oldProteinId"
                       @local-blastp="local_blastp"
            ></sequences>
          </q-tab-panel>

          <q-tab-panel name="homologs">
            <homologs :locus_tag.sync="locus_tag"></homologs>
          </q-tab-panel>

          <q-tab-panel name="environment">
            <environment :locus_tag.sync="locus_tag"></environment>
          </q-tab-panel>

          <q-tab-panel name="references">
            <references></references>
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
import {convertKey} from '../../utils/constants';

import {mapMutations, mapState} from "vuex";

const SCOPE = process.env.APP_SCOPE_NAME
export default {
  name: "cyano_detail",
  data() {
    return {
      isHomologed: true,
      tab: 'jbrowse',
      code: "",
      panel: 'locus_tag',
      data1: null,
      data2: null,
      label: null,
      locus_tag: null,
      refSeqNo: null,
      oldStart: null,
      oldEnd: null,
      oldChr: null,
      oldStrand: null,
      oldProteinId: null,
    }
  },
  methods: {
    local_blastp(data) {
      this.tab = data
    },
    ...mapMutations(SCOPE, ['changeLocus_tag']),
    ...mapMutations(SCOPE, ['changeDefaultSequence']),
    default_seq() {
      this.changeDefaultSequence('child_sequence')
    },
    convertKey(key) {
      return convertKey(key)
    }
  },
  created() {
    this.$q.loading.show({
      message: "Some important <b>process</b> is in progress!"
    })
    http.search_detail({"mg_type": "display", "q": this.$route.params.code}, (res) => {
      this.code = res.data.data.locus_tag
      this.changeLocus_tag(res.data.data.locus_tag)
      this.locus_tag = res.data.data.locus_tag
      this.data1 = res.data.data.data1
      this.data2 = res.data.data.data2
      this.label = res.data.data.label
      this.refSeqNo = res.data.data.ref_seq_no
      this.oldStart = res.data.data.start
      this.oldEnd = res.data.data.end
      this.oldChr = res.data.data.chr
      this.oldStrand = res.data.data.strand
      this.oldProteinId = res.data.data.protein_id
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
