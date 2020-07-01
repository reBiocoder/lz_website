<template>
  <iframe ref="iframe" width="101%" height="99%" id="bdIframe" scrolling="auto" :src="bdTokenUrl"
          frameborder="0"></iframe>
</template>

<script>
  export default {
    name: "jbrowse",
    data() {
      return {
        loc: "0..10000",
        bdTokenUrl: null,
      }
    },
    props: ['ref_seq_no', 'start', 'end', 'chr'],
    mounted() {
      if (this.start !== null && this.end !== null && this.ref_seq_no !==null && this.chr !== null) {
        if((parseInt(this.start)-5000) > 0){
         this.loc = `${parseInt(this.start) - 5000}..${parseInt(this.end) + 5000}`
        }
        else{
          this.loc = `${this.start}..${parseInt(this.end) + 5000}`
        }
        this.bdTokenUrl = `http://122.152.195.44:8001/?data=all_tracks/${this.ref_seq_no}&loc=${this.chr}:${this.loc}&tracks=DNA,${this.ref_seq_no}&highlight=${this.chr}:${this.start}..${this.end}`
      }
      /**
       * iframe-宽高自适应显示
       */
      const oIframe = document.getElementById('bdIframe');
      const deviceWidth = document.documentElement.clientWidth;
      const deviceHeight = document.documentElement.clientHeight;
      oIframe.style.width = (Number(deviceWidth) - 40) + 'px'; //数字是页面布局宽度差值
      oIframe.style.height = (Number(deviceHeight) - 50) + 'px'; //数字是页面布局高度差
      let that = this;
      if (oIframe.attachEvent) {
        oIframe.attachEvent("onload", function () {
          //iframe加载完成后你需要进行的操作
        });
      } else {
        oIframe.onload = function () {
          //iframe加载完成后你需要进行的操作
        };
      }
    },
  }
</script>

<style scoped>

</style>
