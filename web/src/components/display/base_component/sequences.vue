<template>
  <div>
    <div class="row" style="margin-bottom: 10px;">
      <div class="col-9">
        <component  :is="child"
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
      </div>
      <div class="col-3">
        <q-card class="q-ma-sm" style="background: #EAEAEA">
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
        <q-card class="q-ma-sm" style="background: #EAEAEA">
          <q-card-section>
            <div class="text-brown-14 text-bold" style="margin-bottom: 5px;">Further sequence analysis</div>
            <div class="row">
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

  export default {
    name: "sequences",
    data() {
      return {
        title: '',
        from: this.Lstart,
        to: this.Lend,
        child: "child_sequence",
        seq:'',
      }
    },
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
    components:{
      "child_sequence": sequence,
      "blastp": blastp,
    },
    props: ['ref_no', 'chr', 'strand', 'start', 'end', 'Lstart', 'Lend', 'locus_tag'],
  }
</script>

<style scoped>

</style>
