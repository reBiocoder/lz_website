<template>
  <div>
    <q-item :focused="false" :active="false" :clickable="false" :manual-focus="false">
      <q-item-section class="text-center">蓝藻数据库后台管理系统</q-item-section>
    </q-item>
    <q-separator/>

    <q-list v-for="(value, key, index) in asideList" class="rounded-borders" :key="index">

      <q-item v-if="!value.children" clickable v-ripple :to="{name:key}" @click="saveName(value.name)">
        <q-item-section avatar>
          <q-icon :name="value.icon"/>
        </q-item-section>

        <q-item-section>{{ value.name }}</q-item-section>
      </q-item>

      <q-expansion-item
        :icon="value.icon"
        :label="value.name"
        :caption="value.caption"
        v-else
      >

        <q-item v-for="(child_value, child_key, child_index) in value.children" clickable v-ripple :key="child_index"
                :to="{name: child_key}"  @click="saveName(child_value.name)">
          <q-item-section avatar>
            <q-icon :name="child_value.icon"/>
          </q-item-section>
          <q-item-section>{{ child_value.name }}</q-item-section>
        </q-item>

      </q-expansion-item>

    </q-list>
  </div>
</template>

<script>
  import {asideList} from '../../utils/constants';
  import {mapMutations, mapState} from "vuex";

  export default {
    name: "mgAside",
    data() {
      return {
        asideList: asideList,
      }
    },
    methods: {
      ...mapMutations(process.env.APP_SCOPE_NAME, ['changeClickTitle']),
      saveName(name) {
        this.changeClickTitle(name); //将其放入vuex中
      },
    },
    mounted() {
    }
  }
</script>

<style scoped>

</style>
