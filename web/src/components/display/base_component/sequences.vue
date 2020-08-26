<template>
  <div>
    <div class="row" style="margin-bottom: 10px;">
      <div class="col-9">
        <keep-alive include="sequence">
          <component :is="child"
                     :child_protein_id="protein_id"
                     :ref_no="ref_no"
                     :chr="chr"
                     :strand="strand"
                     :Lstart="Lstart"
                     :Lend="Lend"
                     :locus_tag="locus_tag"
                     :re_seq="seq"
                     :re_title="title"
                     :from="from"
                     :to="to"
          >
          </component>
        </keep-alive>
      </div>
      <div class="col-3">
        <q-card class="q-ma-sm" style="background: #EAEAEA">
          <q-card-section>
            <div class="text-brown-14 text-bold" style="margin-bottom: 5px;">Change region shown</div>
            <div class="row">
              <div class="justify-end">
                <div class="col-6">
                  <label for="from">from:</label><input @keyup.enter="update_seq" v-model="from"
                                                        style="width: 65px;margin-right: 5px;" id="from"
                                                        type="text"/>
                </div>
              </div>
              <div class="justify-end">
                <div class="col-6">
                  <label for="to"></label>to:<input @keyup.enter="update_seq" v-model="to"
                                                    style="width: 65px; margin-right: 10px;" id="to"
                                                    type="text"/>
                </div>
              </div>
              <div class="col-3">
                <button @click="update_seq" @keyup.enter="update_seq">Update</button>
              </div>
            </div>
            <div class="row" style="margin-top: 5px;">
              <div class="col-9">
              </div>
            </div>
          </q-card-section>
        </q-card>
        <q-card class="q-ma-sm" style="background: #EAEAEA">
          <q-card-section>
            <div class="text-brown-14 text-bold" style="margin-bottom: 5px;">Further sequence analysis</div>
            <div class="row">
              <q-btn @click="local_interpro" class="col-12 q-ma-sm" color="purple" label="Interproscan"/>
              <q-btn @click="local_blastp" class="col-12 q-ma-sm" color="deep-orange" label="Local BlastP"/>
              <q-btn @click="online_blastp" class="col-12 q-ma-sm" color="primary" label="Online BlastP"/>
              <q-btn @click="online_blastn" class="col-12 q-ma-sm" color="secondary" label="Online BlastN"/>
              <q-btn @click="online_blastx" class="col-12 q-ma-sm" color="amber" label="Online BlastX"/>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
import http from '../../../api/display'
import blastp from "components/display/base_component/child_component/blastp";
import sequence from "components/display/base_component/child_component/sequence";
import blastn from "components/display/base_component/child_component/blastn";
import blastx from "components/display/base_component/child_component/blastx";
import interpro from "components/display/base_component/child_component/interpro";
import {mapMutations,mapState} from "vuex";

const SCOPE = process.env.APP_SCOPE_NAME

export default {
  name: "sequences",
  data() {
    return {
      title: '',
      from: this.Lstart,
      to: this.Lend,
      child: "child_sequence",
      seq: '',
    }
  },
  watch: {
    default_sequence(n, o){
      if(n === 'child_sequence'){  //切换成初始的默认sequence
        this.child = n
      }
    }
  },
  components: {
    "child_sequence": sequence,
    "blastp": blastp,
    'blastn': blastn,
    'blastx': blastx,
    'interpro': interpro,
  },
  computed:{
    ...mapState(SCOPE, ['default_sequence'])
  },
  methods: {
    ...mapMutations(SCOPE, ['changeDnaSequence', 'changeDefaultSequence']),
    local_interpro: function () {
      this.child = 'interpro'  //切换为互扫描组件
      this.changeDefaultSequence('interpro')
    },
    local_blastp: function () {
      this.$emit('local-blastp', 'homologs')
      this.changeDefaultSequence('homologs')
    },
    online_blastx: function () {  // 点击在线blastx按钮
      this.child = 'blastx' //切换为blast组件
      this.changeDefaultSequence('blastx')
    },
    online_blastp: function () {  // 点击在线blastp按钮
      this.child = 'blastp' //切换为blast组件
      this.changeDefaultSequence('blastp')
    },
    online_blastn: function () {  //点击在线blastn按钮
      this.child = 'blastn'
      this.changeDefaultSequence('blastn')
    },
    update_seq: function () { //更新seq序列函数
      this.child = 'child_sequence' //切换组件
      let send_data = {
        'refseq_no': this.ref_no,
        'chr': this.chr,
        'strand': this.strand,
        'start': this.from,
        'end': this.to,
        'Lstart': this.Lstart,
        'Lend': this.Lend,
        "locus_tag": this.locus_tag,
      }
      http.get_sequence(send_data, (res) => {
        if (res.data.code === "success") {
          if (res.data.data === {}) {
            this.$q.notify({
              message: "Please Refresh!"
            })
          } else {  //成功得到数据
            this.title = res.data.data['title']
            let color_start = res.data.data['color_start']
            let color_end = res.data.data['color_end']
            let tmp_seq = res.data.data['seq']
            this.changeDnaSequence(tmp_seq)  //更新vuex
            if (color_start !== -1 && color_end !== -1) {
              let orf = tmp_seq.toString().substring(color_start, color_end)
              let color_orf = "<span class='text-uppercase' style='color: blue'>" + orf + "</span>"
              //this.seq = orf
              this.seq = tmp_seq.toString().replace(orf, color_orf)
            } else {
              this.seq = tmp_seq
            }
          }
        } else {
          this.$q.notify({
            message: "Error! Try again"
          })
        }

      })
    }
  },
  props: ['ref_no', 'chr', 'strand', 'start', 'end', 'Lstart', 'Lend', 'locus_tag', 'protein_id'],
}
</script>

<style scoped>

</style>
