(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[4],{3325:function(e,t,a){},4536:function(e,t,a){e.exports=a.p+"img/logo.d3223fd5.svg"},cd9d:function(e,t,a){"use strict";var r=a("3325"),n=a.n(r);n.a},f8a7:function(e,t,a){"use strict";a.r(t);var r=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("q-layout",{staticClass:"bg-grey-1",attrs:{view:"hHh lpR fFf"}},[r("q-header",{staticClass:"bg-white text-grey-8 q-py-xs",attrs:{elevated:"","height-hint":"58"}},[r("q-toolbar",[r("q-btn",{attrs:{flat:"",dense:"",round:"","aria-label":"Menu",icon:"menu"},on:{click:function(t){e.leftDrawerOpen=!e.leftDrawerOpen}}}),e.$q.screen.gt.xs?r("q-btn",{staticClass:"q-ml-xs",attrs:{flat:"","no-caps":"","no-wrap":""},on:{click:e.to_index}},[r("img",{staticStyle:{height:"45px"},attrs:{src:a("4536"),alt:"logo"}})]):e._e(),r("q-space"),r("div",{staticClass:"YL__toolbar-input-container row no-wrap"},[r("q-input",{staticClass:"bg-white col",attrs:{dense:"",outlined:"",square:"",placeholder:"Search"},on:{keyup:function(t){return!t.type.indexOf("key")&&e._k(t.keyCode,"enter",13,t.key,"Enter")?null:e.getSearch(t)}},scopedSlots:e._u([{key:"before",fn:function(){return[r("q-select",{attrs:{borderless:"","display-value":e.select_search_label,options:e.options,dense:""},model:{value:e.select_search,callback:function(t){e.select_search=t},expression:"select_search"}})]},proxy:!0}]),model:{value:e.search,callback:function(t){e.search=t},expression:"search"}}),r("q-btn",{staticClass:"YL__toolbar-input-btn",attrs:{color:"grey-3","text-color":"grey-8",icon:"search",unelevated:""},on:{click:e.getSearch}})],1),r("q-space"),r("div",{staticClass:"q-gutter-sm row items-center no-wrap"})],1)],1),r("q-drawer",{attrs:{bordered:"",width:200,mini:e.miniState},model:{value:e.leftDrawerOpen,callback:function(t){e.leftDrawerOpen=t},expression:"leftDrawerOpen"}},[r("q-scroll-area",{staticClass:"fit"},[r("q-list",{attrs:{padding:""}},[e._l(e.links1,(function(t){return r("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],key:t.text,attrs:{clickable:""},on:{click:function(a){return e.func(t.code)}}},[r("q-item-section",{attrs:{avatar:""}},[r("q-icon",{attrs:{color:"grey",name:t.icon}})],1),r("q-item-section",[r("q-item-label",[e._v(e._s(t.text))])],1),r("q-tooltip",{attrs:{anchor:"center right",self:"center left",offset:[10,10],"transition-show":"rotate","transition-hide":"rotate"}},[e._v("\n            "+e._s(t.text)+"\n          ")])],1)})),e._l(e.links2,(function(t){return r("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],key:t.text,attrs:{clickable:""},on:{click:function(a){return e.func(t.code)}}},[r("q-item-section",{attrs:{avatar:""}},[r("q-icon",{attrs:{color:"grey",name:t.icon}})],1),r("q-item-section",[r("q-item-label",[e._v(e._s(t.text))])],1),r("q-tooltip",{attrs:{anchor:"center right",self:"center left",offset:[10,10],"transition-show":"rotate","transition-hide":"rotate"}},[e._v("\n            "+e._s(t.text)+"\n          ")])],1)})),r("q-separator",{staticClass:"q-mt-md q-mb-xs"})],2)],1)],1),r("q-page-container",[r("keep-alive",{attrs:{include:"cyano,index,cyano_detail"}},[r("router-view",{key:this.$route.fullPath})],1)],1)],1)},n=[],s=(a("8e6e"),a("8a81"),a("ac6a"),a("cadf"),a("06db"),a("456d"),a("386d"),a("c47a")),c=a.n(s),o=a("d272"),l=a("2f62");function i(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);t&&(r=r.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,r)}return a}function u(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?i(Object(a),!0).forEach((function(t){c()(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):i(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var h={name:"MyLayout",data:function(){return{select_search_label:null,select_search:null,select_search_result:null,options:[{label:"Global",value:"cyano_all_gff_all"},{label:"Species",value:"cyano_genomes"},{label:"Gene",value:"cyano_all_gff"},{label:"Annotation",value:"cyano_all_gff_product"}],miniState:!0,logo:o["a"],leftDrawerOpen:!0,search:"",links1:[{icon:"home",text:"Data Set",code:"index"}],links2:[{icon:"description",text:"Hot",code:"hot"},{icon:"web",text:"Recent publications",code:"pubmed"}]}},watch:{select_search:{handler:function(e,t){this.select_search_label=void 0===e.label?this.options[0].label:e.label,this.select_search_result=void 0===e.value?this.options[0].value:e.value}}},mounted:function(){this.select_search_label=this.options[0].label,this.select_search=this.options[0].value},methods:u(u({},Object(l["b"])("lz_website",["changeSearchContent"])),{},{admin:function(){this.$router.push({name:"login"})},getSearch:function(){""===this.search?this.$q.notify({message:"Please input search content"}):(this.changeSearchContent(this.search),"cyano_genomes"===this.select_search_result?this.$router.push({name:"search_species",query:{q:this.search}}):"cyano_all_gff"===this.select_search_result?this.$router.push({name:"search_gene",query:{q:this.search}}):"cyano_all_gff_all"===this.select_search_result?this.$router.push({name:"search_all",query:{q:this.search}}):"cyano_all_gff_product"===this.select_search_result&&this.$router.push({name:"search_product",query:{q:this.search}}))},to_index:function(){this.$router.push({name:"index"})},func:function(e){this.$router.push({name:e})}})},p=h,f=(a("cd9d"),a("2877")),d=a("4d5a"),_=a("e359"),b=a("65c6"),m=a("9c40"),y=a("6ac5"),g=a("2c91"),q=a("27f9"),v=a("ddd8"),w=a("cb32"),x=a("0016"),k=a("05c0"),O=a("9404"),Q=a("4983"),S=a("1c1c"),j=a("66e5"),C=a("4074"),D=a("0170"),P=a("eb85"),$=a("09e3"),L=a("8572"),I=a("714f"),E=a("eebe"),T=a.n(E),A=Object(f["a"])(p,r,n,!1,null,null,null);t["default"]=A.exports;T()(A,"components",{QLayout:d["a"],QHeader:_["a"],QToolbar:b["a"],QBtn:m["a"],QToolbarTitle:y["a"],QSpace:g["a"],QInput:q["a"],QSelect:v["a"],QAvatar:w["a"],QIcon:x["a"],QTooltip:k["a"],QDrawer:O["a"],QScrollArea:Q["a"],QList:S["a"],QItem:j["a"],QItemSection:C["a"],QItemLabel:D["a"],QSeparator:P["a"],QPageContainer:$["a"],QField:L["a"]}),T()(A,"directives",{Ripple:I["a"]})}}]);