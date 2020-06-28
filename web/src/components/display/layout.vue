<template>
  <q-layout view="hHh lpR fFf" class="bg-grey-1">
    <q-header elevated class="bg-white text-grey-8 q-py-xs" height-hint="58">
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
        />
        <q-btn flat no-caps no-wrap class="q-ml-xs" @click="to_index" v-if="$q.screen.gt.xs">
          <q-icon :name="logo" color="red" size="28px"/>
          <q-toolbar-title shrink class="text-weight-bold">
            Cyanobacteria Database
          </q-toolbar-title>
        </q-btn>

        <q-space/>

        <div class="YL__toolbar-input-container row no-wrap">
          <q-input dense outlined square v-model="search" @keyup.enter="getSearch" placeholder="Search"
                   class="bg-white col">
            <template v-slot:before>
              <q-select  borderless :display-value="select_search_label" v-model="select_search" :options="options" dense/>
            </template>
          </q-input>
          <q-btn class="YL__toolbar-input-btn" @click="getSearch" color="grey-3" text-color="grey-8" icon="search"
                 unelevated/>
        </div>

        <q-space/>

        <div class="q-gutter-sm row items-center no-wrap">
          <!--          <q-btn @click="admin" round flat>-->
          <!--            <q-avatar size="26px">-->
          <!--              <q-icon color="grey" name="account_circle"/>-->
          <!--            </q-avatar>-->
          <!--            <q-tooltip>管理员登录</q-tooltip>-->
          <!--          </q-btn>-->
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      bordered
      :width="200"
      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"
    >
      <q-scroll-area class="fit">
        <q-list padding>
          <q-item v-for="link in links1" :key="link.text" @click="func(link.code)" v-ripple clickable>
            <q-item-section avatar>
              <q-icon color="grey" :name="link.icon"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ link.text }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-separator class="q-my-md"/>

          <q-item v-for="link in links2" @click="func(link.code)" :key="link.text" v-ripple clickable>
            <q-item-section avatar>
              <q-icon color="grey" :name="link.icon"/>
            </q-item-section>
            <q-item-section>
              <q-item-label>{{ link.text }}</q-item-label>
            </q-item-section>
          </q-item>

          <q-separator class="q-mt-md q-mb-xs"/>

        </q-list>
      </q-scroll-area>
    </q-drawer>

    <q-page-container>
      <keep-alive include="cyano,index,cyano_detail">
        <router-view :key="this.$route.fullPath"/>
      </keep-alive>
    </q-page-container>
  </q-layout>
</template>

<script>
  import {farSmileWink} from '@quasar/extras/fontawesome-v5'
  import {mapMutations} from 'vuex'

  export default {
    name: 'MyLayout',
    data() {
      return {
        select_search_label: null,
        select_search: null,
        select_search_result: null,
        options: [
          {label: "Species", value: "cyano_genomes"},
          {label: "Gene", value: "cyano_all_gff"}
        ],
        miniState: true,
        logo: farSmileWink,
        leftDrawerOpen: true,
        search: '',
        links1: [
          {icon: 'home', text: 'Data Set', code: "index"},  // 首页
          //{icon: 'whatshot', text: 'Trending', code:"trending"}, //趋势
        ],
        links2: [
          {icon: 'description', text: 'Hot', code: "hot"},
          {icon: 'web', text: 'JBrowse', code: "jbrowse"},
          {icon: 'description', text: 'PubMed', code: "pubmed"},
        ]
      }
    },
    watch:{
      select_search:{
        handler:function (newVal, oldVal) {
          this.select_search_label = newVal.label === undefined ? this.options[0].label : newVal.label
          this.select_search_result = newVal.value === undefined ? this.options[0].value : newVal.value
          console.log("我的值:"+this.select_search_result)
        }
      }
    },
    mounted() {
      this.select_search_label = this.options[0].label
      this.select_search = this.options[0].value
    },
    methods: {
      ...mapMutations(process.env.APP_SCOPE_NAME, ["changeSearchContent"]),
      //管理员登录,跳转
      admin() {
        this.$router.push({
          name: "login"
        })
      },
      //用户搜索得到结果
      getSearch() {
        if (this.search === "") {
          this.$q.notify({
            message: "Please input search content"
          })
        } else {
          this.changeSearchContent(this.search)
          this.$router.push({name: "search", params: {code: this.search}})
        }

      },
      // 点击logo,跳转到首页
      to_index() {
        this.$router.push({
          name: "index"
        })
      },
      //点击边页功能
      func(code) {
        this.$router.push({
          name: code
        })
      },
    },
  }
</script>

<style lang="sass">
  .q-field--dense
    .q-field__before, .q-field__prepend
      padding-right: 0px

    .q-field__native, .q-field__prefix, .q-field__suffix, .q-field__input
      font-weight: 400
      line-height: 28px
      letter-spacing: 0.00937em
      text-decoration: inherit
      text-transform: inherit
      border: none
      border-radius: 0
      background: none
      color: rgba(0, 0, 0, 0.87)
      padding: 6px 0px 6px 10px

  .YL
    &__toolbar-input-container
      min-width: 100px
      width: 55%

    &__toolbar-input-btn
      border-radius: 0
      border-style: solid
      border-width: 1px 1px 1px 0
      border-color: rgba(0, 0, 0, .24)
      max-width: 60px
      width: 100%

    &__drawer-footer-link
      color: inherit
      text-decoration: none
      font-weight: 500
      font-size: .75rem

      &:hover
        color: #000

</style>
