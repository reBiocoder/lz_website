<template>
  <div>
    <span class="setting-left">
      <q-btn @click="into_blastx" style="background: goldenrod; color: white"
             label="full screen"
      />
    </span>
    <iframe ref="iframe" width="100%" height="150%" id="blastp"
            scrolling="auto" :src="bdTokenUrl"
            frameborder="0">
    </iframe>
    <q-inner-loading :showing="visible">
      <q-spinner-gears size="50px" color="primary"/>
      <p class="text-purple text-body1">
        The InterProScan is loading,please wait a few seconds...
      </p>
    </q-inner-loading>
  </div>
</template>

<script>
  import http from '../../../../api/display'

  export default {
    name: "interpro",
    data() {
      return {
        bdTokenUrl: "",
        visible: true,
        name: '',
      }
    },
    methods: {
      into_blastx() {
        window.open(this.bdTokenUrl, "_blank")
      }
    },
    mounted() {
      http.get_interpro({"ref_no": this.ref_no, "locus_tag": this.locus_tag},
        (res) => {
          let base_url = `http://124.70.143.103:18883/`
          this.name = res.data.data.name
          if (this.name === '') {
            this.bdTokenUrl = base_url + 'index.html'
          } else {
            this.bdTokenUrl = base_url + this.name
          }
          const oIframe = document.getElementById('blastp');
          const deviceHeight = document.documentElement.clientHeight;
          oIframe.style.height = (Number(deviceHeight) - 50) + 'px'; //数字是页面布局高度差
          let that = this;
          if (oIframe.attachEvent) {
            oIframe.attachEvent("onload", function () {
              //iframe加载完成后你需要进行的操作
              that.visible = false
            });
          } else {
            oIframe.onload = function () {
              //iframe加载完成后你需要进行的操作
              that.visible = false
            };
          }
        })
    },
    props: ['ref_no', 'locus_tag'],
  }
</script>

<style scoped>
  .setting-left {
    top: 20px;
    bottom: 0;
    left: 0;
    position: absolute;
    height: 36px;
  }

</style>
