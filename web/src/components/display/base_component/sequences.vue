<template>
  <div>
    <div class="row" style="margin-bottom: 10px;">
      <div class="col-9">
        <div class="row">
          <div class="text-h5" style="margin-bottom: 20px;">Selected nucleotide sequences<span
            style="color: blue;font-size: 18px;margin-left: 10px;">tips:The open reading frame of [{{ this.locus_tag }}] is shown in blue font</span>:
          </div>
        </div>

        <div class="row">
          <div style="margin-bottom: 0px; font-size: 17px;">{{this.title}}</div>
          <pre v-html="seq" class="pre-text text-lowercase text-justify"></pre>
        </div>

        <div class="row">
          <div class="text-h5" style="margin-bottom: 20px;margin-top: 20px;">Amino acid sequences:</div>
        </div>
        <div>
          <div style="margin-bottom: 0px; font-size: 17px;">{{this.faa_title}}</div>
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
      <div class="col-3">
        <q-card style="background: #EAEAEA">
          <q-card-section>
            <div class="text-brown-14 text-bold" style="margin-bottom: 5px;">Change region shown</div>
            <div class="row">
              <div class="justify-end">
                <div class="col-6">
                  <label for="from">from:</label><input @keyup.enter="update_seq" v-model="from"
                                                        style="width: 80px;margin-right: 5px;" id="from"
                                                        type="text"/>
                </div>
              </div>
              <div class="justify-end">
                <div class="col-5">
                  <label for="to"></label>to:<input @keyup.enter="update_seq" v-model="to"
                                                    style="width: 80px; margin-right: 10px;" id="to"
                                                    type="text"/>
                </div>
              </div>
              <div class="col-1">
                <button @click="update_seq" @keyup.enter="update_seq">Update</button>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </div>
</template>

<script>
  import http from '../../../api/display'

  export default {
    name: "sequences",
    data() {
      return {
        visible: true,
        from: this.Lstart,
        to: this.Lend,
        title: '',
        seq: '',
        faa_content: '',
        faa_title: '',
      }
    },
    props: ['ref_no', 'chr', 'strand', 'start', 'end', 'Lstart', 'Lend', 'locus_tag'],
    methods: {
      update_seq: function () {
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
