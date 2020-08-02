<template>
  <div>
    <span class="setting-left">
      <q-btn @click="into_blastn" style="background: goldenrod; color: white"
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
        The online BlastN is loading,it can do some customization,please wait a few seconds...
        </p>
    </q-inner-loading>
    </div>
</template>

<script>
    export default {
      name: "blastn",
      data(){
          return{
            bdTokenUrl: "",
            visible: true,
          }
      },
      methods:{
        into_blastn(){
          window.open(this.bdTokenUrl, "_blank")
        }
      },
      mounted() {
        let url = `https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=Nucleotides&PROGRAM=blastn&QUERY=${this.chr}&DATABASE=nr&MEGABLAST=on&BLAST_PROGRAMS=blastn&LINK_LOC=nuccore&PAGE_TYPE=BlastSearch&QUERY_FROM=${this.from}&QUERY_TO=${this.to}`
        this.bdTokenUrl = url
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
      },
      props:['chr', 'from', 'to'],
    }
</script>

<style scoped>
  .setting-left{
    top: 20px;
    bottom: 0;
    left: 0;
    position: absolute;
    height: 36px;
  }
</style>
