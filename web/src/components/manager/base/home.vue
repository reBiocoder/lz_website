<template>
  <div class="q-pa-md">
    <q-card>
      <q-tab-panel name="picture" class="shadow-0">
        <div class="text-h6 text-primary">访问统计图</div>
        <q-separator/>

        <div ref="chart1" style="width:100%;height:376px"></div>

      </q-tab-panel>
    </q-card>
  </div>
</template>

<script>
  import http from '../../../api/backStage.js'
  export default {
    name: "home",
    data() {
      return {}
    },
    mounted() {
      http.get_access((res) => {
        this.getEchartData1(res)
      })
    },
    methods: {
      getEchartData1(res) {  //得到首页echart图
        const chart1 = this.$refs.chart1;
        if (chart1) {
          const myChart = this.$echarts.init(
            chart1
          );
          let option = {
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'cross',
                label: {
                  backgroundColor: '#6a7985'
                }
              }
            },
            legend: {
              data: ['最近一周接口访问量']
            },
            toolbox: {
              feature: {
                saveAsImage: {}
              }
            },
            grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
            },
            xAxis: [
              {
                type: 'category',
                boundaryGap: false,
                data: res.data.data["x_data"]  //横坐标数据
              }
            ],
            yAxis: [
              {
                type: 'value'
              }
            ],
            series: res.data.data["series_data"]  //series数据
          };
          myChart.setOption(option, true);
        }
      }
    }
  }
</script>

<style scoped>

</style>
