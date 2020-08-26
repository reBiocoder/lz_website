<template>
  <div>
    <span class="setting-left">
      <q-btn @click="into_blastp" style="background: goldenrod; color: white"
             label="full screen"
      />
    </span>
    <iframe ref="iframe" width="100%" height="150%" id="blastp"
            scrolling="auto" :src="bdTokenUrl"
            frameborder="0">
    </iframe>
    <q-inner-loading :showing="visible">
      <q-spinner-gears size="50px" color="primary"/>
      <p class="text-purple text-body1" style="margin-bottom: 0px;">
        The KEGG is loading,please wait a few seconds...
      </p>
      <p>
        <span class="text-orange-8">
          Tip: if this page prompts "Link reset", please use the "FULL SCREEN" button to open this page
        </span>
      </p>
    </q-inner-loading>
  </div>
</template>

<script>
import http from '../../../../api/display'

export default {
  name: "kegg",
  data() {
    return {
      bdTokenUrl: "",
      visible: true,
      kegg: null
    }
  },
  methods: {
    into_blastp() {
      window.open(this.bdTokenUrl, "_blank")
    }
  },
  mounted() {
    http.get_kegg({'ref_no': this.ref_no}, (res) => {
      this.kegg = res.data.data.kegg_no
      if (this.old_locus_tag.indexOf("%2C") !== -1) { //存在%2c
        this.old_locus_tag = this.old_locus_tag.split("%2C")[1]
      }
      if (this.old_locus_tag !== null) {
        window.myurl = `https://www.genome.jp/dbget-bin/www_bget?${this.kegg}:${this.old_locus_tag}`
      } else {
        window.myurl = `https://www.genome.jp/dbget-bin/www_bget`
      }
      this.bdTokenUrl = window.myurl
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
  props: ['old_locus_tag', 'ref_no'],
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
