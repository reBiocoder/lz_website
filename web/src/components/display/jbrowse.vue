<template>
  <div>
    <iframe ref="iframe" width="101%" height="99%" id="bdIframe" scrolling="auto" :src="bdTokenUrl"
            frameborder="0"></iframe>
  </div>
</template>

<script>
  export default {
    name: "jbrowse",
    data() {
      return {
        bdTokenUrl: 'https://jbrowse.org/code/JBrowse-1.16.8/?data=sample_data%2Fjson%2Fvolvox&tracklist=1&nav=1&overview=1&tracks=DNA%2CExampleFeatures%2CNameTest%2CMotifs%2CGenes%2CReadingFrame%2CCDS%2CTranscript%2CClones%2CEST&loc=ctgA%3A12423..33834&highlight='
      }
    },
    mounted() {
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
