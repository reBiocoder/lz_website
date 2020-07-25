<template>
  <div>
    <div class="row" style="margin-bottom: 10px;">
      <div class="col-9">
        <div class="row">
          <div class="text-h5" style="margin-bottom: 20px;">Nuleotide sequences:</div>
        </div>
        <div class="row">
          <div style="margin-bottom: 0px; font-size: 17px;">{{this.title}}</div>
          <pre style="margin-top: 0px; font-size: 15px;" class="text-justify">{{this.seq}}</pre>
        </div>
      </div>
      <div class="col-3">
        <q-card style="background: #EAEAEA">
          <q-card-section>
            <div class="text-brown-14 text-bold" style="margin-bottom: 5px;">Change region shown</div>
            <div class="row">
              <div class="justify-end">
                <div class="col-6">
                  <label for="from">from:</label><input style="width: 80px;margin-right: 5px;" id="from" type="text"/>
                </div>
              </div>
              <div class="justify-end">
              <div class="col-5">
                <label for="to"></label>to:<input style="width: 80px; margin-right: 10px;" id="to" type="text"/>
              </div>
              </div>
              <div class="col-1">
                <button>Update</button>
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
        search_input: 'abc',
        text: '',
        title: '',
        seq: ''
      }
    },
    mounted() {
      http.get_sequence({}, (res) => {
        console.log(res)
        if (res.data.code === "success") {
          if (res.data.data === {}) {
            this.$q.notify({
              message: "Please Refresh!"
            })
          } else {
            this.title = res.data.data['title']
            this.seq = res.data.data['seq']
          }
        } else {
          this.$q.notify({
            message: "Error! Try again"
          })
        }

      })
    }
  }
</script>

<style scoped>
  .seq-input {
    width: 80px;
  }
</style>
