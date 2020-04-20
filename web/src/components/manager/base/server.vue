<template>
  <div class="q-pa-md">
    <q-card>
      <q-tab-panel name="locus_tag">
        <div class="text-h5">服务器信息</div>
        <q-badge color="purple">server</q-badge>
      </q-tab-panel>
      <div class="messageBlock">
        <div class="messageBox1"><p><span class="messageLabel ng-binding">实例ID:</span> <span
          class="messageContent ng-binding">919c9cdc53e747d79c5ef5fbe7b6db63</span></p>
          <p><span class="messageLabel ng-binding">IP地址:</span> <span class="messageContent ng-binding">(公) 119.23.246.30 (内) 172.16.15.152</span>
          </p>
          <p><span class="messageLabel ng-binding">DDos攻击状态:</span> <span class="messageContent"><!-- ngIf: currentServerMsg.DdosStatus === 'normal' --><span
            ng-if="currentServerMsg.DdosStatus === 'normal'" style="color: #6FCE7F"
            class="ng-scope ng-binding">正常</span><!-- end ngIf: currentServerMsg.DdosStatus === 'normal' -->
            <!-- ngIf: currentServerMsg.DdosStatus === 'blackhole' -->
            <!-- ngIf: currentServerMsg.DdosStatus === 'defense' --></span></p></div>
        <div class="messageBox2"><p><span class="messageLabel ng-binding">镜像信息:</span> <span
          class="messageContent ng-binding"><img ng-src="https://gw.alicdn.com/mt/TB1dnnOa_ZRMeJjSspkXXXGpXXa-60-60.png"
                                                 class="messageImage"
                                                 src="https://gw.alicdn.com/mt/TB1dnnOa_ZRMeJjSspkXXXGpXXa-60-60.png">Ubuntu 18.04</span>
        </p><!-- ngIf: chargeType === 'PrePaid' --><p ng-if="chargeType === 'PrePaid'" class="ng-scope"><span
          class="messageLabel ng-binding">到期日期:</span> <span
          class="messageContent ng-binding">2021-06-08 00:00:00</span></p><!-- end ngIf: chargeType === 'PrePaid' -->
          <!-- ngIf: chargeType === 'PostPaid' --></div>
        <div class="messageBox3"><!-- ngIf: chargeType === 'PrePaid' --><p ng-if="chargeType === 'PrePaid'"
                                                                           class="ng-scope"><a
          class="messageLink ng-binding" ng-click="confirmUpgrade()" aliyun-console-spm="6" href="javascript:void(0);"
          data-spm-click="gostr=/aliyun;locaid=d6;;">升级</a> <a class="messageLink ng-binding"
                                                               href="https://common-buy.aliyun.com?commodityCode=swas&amp;instanceId=919c9cdc53e747d79c5ef5fbe7b6db63&amp;orderType=RENEW#/renew"
                                                               target="_blank" aliyun-console-spm="7"
                                                               data-spm-click="gostr=/aliyun;locaid=d7;;">续费</a></p>
          <!-- end ngIf: chargeType === 'PrePaid' --><p><a class="messageLink ng-binding" ng-click="modifyPassword()"
                                                           aliyun-console-spm="2" href="javascript:void(0);"
                                                           data-spm-click="gostr=/aliyun;locaid=d2;;">重置密码</a></p>
          <p><a class="messageLink ng-binding" ui-sref="server.ops.os" aliyun-console-spm="4"
                href="#/server/919c9cdc53e747d79c5ef5fbe7b6db63/cn-shenzhen/ops/os"
                data-spm-click="gostr=/aliyun;locaid=d4;;">重置系统</a></p></div>
      </div>
    </q-card>
  </div>
</template>

<script>
  export default {
    name: "server"
  }
</script>

<style scoped>
  .messageBlock {
    display: table;
    width: 100%;
    margin-top: 5px;
    padding: 20px;
    background-color: #ffffff;
    box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.2);
  }

  .messageBlock .messageBox1 {
    display: table-cell;
    width: 45%;
  }

  .messageBlock .messageBox2 {
    display: table-cell;
    width: 45%;
  }

  .messageBlock .messageBox3 {
    display: table-cell;
    width: 10%;
    padding-left: 20px;
    border-left: 1px solid #ddd;
  }

  .messageBlock .messageLabel {
    font-size: 14px;
    font-weight: 500;
    margin-right: 10px;
  }

  .messageBlock .messageImage {
    width: 20px;
  }

  .messageTitle {
    margin: 10px 0;
  }
</style>

