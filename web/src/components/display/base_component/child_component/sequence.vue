<template>
  <div>
    <div class="row">
      <div class="text-h5" style="">Selected nucleotide sequences</div>
    </div>
    <div class="row">
      <div
        style="color: blue;font-size: 18px; margin-bottom: 20px;">
        tips:The open reading frame of {{ this.locus_tag }} is shown in blue font
      </div>
    </div>
    <div class="row">
      <div style="margin-bottom: 0px; font-size: 17px;">
        {{ this.title }}
        <q-icon @click="dna_download" style="font-size: 20px;" name="get_app">
          <q-tooltip>
            Download currently selected sequence
          </q-tooltip>
        </q-icon>
      </div>
      <pre v-html="seq" class="pre-text text-lowercase text-justify"></pre>
    </div>

    <div class="row">
      <div class="text-h5" style="margin-bottom: 20px;margin-top: 20px;">Amino acid sequences:</div>
    </div>
    <div>
      <div style="margin-bottom: 0px; font-size: 17px;">
        {{ this.faa_title }}
        <q-icon @click="protein_download" style="font-size: 20px;" name="get_app">
          <q-tooltip>
            Download protein sequence
          </q-tooltip>
        </q-icon>
      </div>
      <pre v-html="faa_content" class="pre-text text-uppercase text-justify">
        </pre>
      <q-inner-loading :showing="visible">
        <q-spinner-gears size="50px" color="primary"/>
        <p class="text-purple text-body1">
          The first load of protein data is a little slow, please wait a few seconds...
        </p>
      </q-inner-loading>
    </div>
  </div>
</template>

<script>
import http from "src/api/display";
import {exportFile} from 'quasar';
import {mapMutations, mapState} from "vuex";

const SCOPE = process.env.APP_SCOPE_NAME

export default {
  name: "sequence",
  data() {
    return {
      visible: true,
      faa_content: '',
      faa_title: '',
      title: '',
      seq: '',
    }
  },
  computed: {
    ...mapState(SCOPE, ['dna_sequence', 'protein_sequence']),
  },
  props: ['ref_no', 'chr', 'strand', 'Lstart', 'Lend',
    'locus_tag', 're_seq', 're_title', 'from', 'to'],
  watch: {
    re_seq(n, o) {
      if (n === '') {
      } else {
        this.seq = n
      }
    },
    re_title(n, o) {
      if (n === '') {
      } else {
        this.title = n
      }
    }
  },
  methods: {
    ...mapMutations(SCOPE, ['changeDnaSequence', 'changeProteinSequence']),
    dna_download() {  // 下载DNA文件
      let str_title = this.ref_no + '_' + this.from + '_' + this.to + '.txt'
      let dna_text = `${this.title}\n${this.dna_sequence}`
      const status = exportFile(str_title, dna_text)
      if (status === true) {
        // 浏览器允许
      } else {
        // 浏览器拒绝
        console.log('Error: ' + status)
      }
    },
    protein_download() { //下载蛋白质文件
      let str_title = this.locus_tag + '_' + this.ref_no + '.txt'
      let faa_text = `${this.faa_title}\n${this.faa_content}`
      const status = exportFile(str_title, faa_text)
      if (status === true) {
        // 浏览器允许
      } else {
        // 浏览器拒绝
        console.log('Error: ' + status)
      }
    }
  },
  mounted() {
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
    http.get_default_sequence((res) => {
      this.visible = false
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
          this.faa_title = res.data.data['faa_title']
          this.faa_content = res.data.data['faa_content']
          this.changeProteinSequence(this.faa_content)
        }
      } else {
        this.$q.notify({
          message: "Error! Try again"
        })
      }

    }, () => {
    }, send_data)
  }
}
</script>

<style scoped>
.pre-text {
  margin-top: 0px;
  font-size: 15px;
  word-wrap: break-word;
  white-space: normal;
  word-break: break-all;
}
</style>
