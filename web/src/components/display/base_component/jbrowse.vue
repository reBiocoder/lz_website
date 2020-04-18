<template>
  <iframe ref="iframe" width="101%" height="99%" id="bdIframe" scrolling="auto" :src="bdTokenUrl"
          frameborder="0"></iframe>
</template>

<script>
  import {mapState} from 'vuex'
  export default {
    name: "jbrowse",
    data() {
      return {
        loc:"0..10000",
        bdTokenUrl: null
      }
    },
    computed:{
      ...mapState(process.env.APP_SCOPE_NAME, ['gene_start','gene_end'])
    },
    mounted() {
      if(this.gene_start !==null && this.gene_end !==null){
        this.loc = `${this.gene_start-1000}..${this.gene_end+1000}`
        this.bdTokenUrl = `http://122.152.195.44:8001/?data=data&loc=${this.loc}`
      }
      this.$q.loadingBar.start()
      /**
       * iframe-宽高自适应显示
       */
      const oIframe = document.getElementById('bdIframe');
      const deviceWidth = document.documentElement.clientWidth;
      const deviceHeight = document.documentElement.clientHeight;
      oIframe.style.width = (Number(deviceWidth) - 240) + 'px'; //数字是页面布局宽度差值
      oIframe.style.height = (Number(deviceHeight) - 50) + 'px'; //数字是页面布局高度差
      let that = this;
      if (oIframe.attachEvent) {
        oIframe.attachEvent("onload", function () {
          //iframe加载完成后你需要进行的操作
          that.$q.loadingBar.stop()
        });
      } else {
        oIframe.onload = function () {
          //iframe加载完成后你需要进行的操作
          that.$q.loadingBar.stop()
        };
      }
    },
  }
</script>

<style scoped>

</style>
