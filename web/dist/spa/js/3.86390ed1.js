(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[3,7,8,15],{"0e52":function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("iframe",{ref:"iframe",attrs:{width:"101%",height:"99%",id:"bdIframe",scrolling:"auto",src:e.bdTokenUrl,frameborder:"0"}})},r=[],o=(a("8e6e"),a("8a81"),a("ac6a"),a("cadf"),a("06db"),a("456d"),a("c5f6"),a("c47a")),i=a.n(o),c=a("2f62");function s(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function l(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?s(Object(a),!0).forEach((function(t){i()(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):s(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var d={name:"jbrowse",data:function(){return{loc:"0..10000",bdTokenUrl:null}},computed:l({},Object(c["c"])("lz_website",["gene_start","gene_end"])),mounted:function(){null!==this.gene_start&&null!==this.gene_end&&(this.loc="".concat(this.gene_start-1e3,"..").concat(this.gene_end+1e3),this.bdTokenUrl="http://122.152.195.44:8001/?data=data&loc=".concat(this.loc)),this.$q.loadingBar.start();var e=document.getElementById("bdIframe"),t=document.documentElement.clientWidth,a=document.documentElement.clientHeight;e.style.width=Number(t)-240+"px",e.style.height=Number(a)-50+"px";var n=this;e.attachEvent?e.attachEvent("onload",(function(){n.$q.loadingBar.stop()})):e.onload=function(){n.$q.loadingBar.stop()}}},u=d,b=a("2877"),p=Object(b["a"])(u,n,r,!1,null,"4f00b4e2",null);t["default"]=p.exports},"9f3c":function(e,t,a){"use strict";var n=a("2b0e"),r=n["a"].prototype.$post,o=n["a"].prototype.$get;t["a"]={index_random_data:function(e){o("api/index_data/",e)},index_random_col:function(e){o("api/index_col/",e)},search_data:function(e,t){r("api/search/",e,t)},search_detail:function(e,t){r("/api/detail/",e,t)},search_environment:function(e,t){r("/api/environment/",e,t)},environment_image:function(e,t){r("/api/get_image/",e,t)},pubmed:function(e,t){r("/api/pubmed/",e,t)}}},a70f:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"q-pa-md"},[a("q-table",{attrs:{title:e.code,data:e.data,columns:e.columns,"row-key":"key",separator:"cell","rows-per-page-options":[0],pagination:e.pagination,"hide-header":!0,"hide-bottom":!0},on:{"update:pagination":function(t){e.pagination=t}},scopedSlots:e._u([{key:"body-cell-key",fn:function(t){return[a("q-td",{staticStyle:{width:"20%","background-color":"rgb(109, 81, 136)"},attrs:{props:t,"auto-width":!1}},[e._v("\n        "+e._s(t.value)+"\n      ")])]}}])})],1)},r=[],o=(a("8e6e"),a("8a81"),a("ac6a"),a("cadf"),a("06db"),a("456d"),a("c47a")),i=a.n(o),c=a("9f3c"),s=a("2f62");function l(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function d(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?l(Object(a),!0).forEach((function(t){i()(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):l(Object(a)).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var u={name:"base_data",data:function(){return{pagination:{page:1,rowsPerPage:0},code:"Detail",columns:[{name:"key",label:"key",field:"key",align:"center"},{name:"value",label:"value",field:"value",align:"center"}],data:[]}},methods:d({},Object(s["b"])("lz_website",["changeGeneStart","changeGeneEnd"])),mounted:function(){var e=this;this.code="Base Information Of ".concat(this.$route.params.code),c["a"].search_detail({q:this.$route.params.code},(function(t){if("success"===t.data.code){e.data=t.data.data,console.log(e.data);for(var a=0,n=e.data.length;a<n;++a)"Start"===e.data[a].key&&e.changeGeneStart(e.data[a].value),"End"===e.data[a].key&&e.changeGeneEnd(e.data[a].value)}else e.$q.notify({message:"Please try again"})}))}},b=u,p=a("2877"),f=a("eebe"),m=a.n(f),g=a("eaac"),h=a("db86"),v=Object(p["a"])(b,n,r,!1,null,"6394b282",null);t["default"]=v.exports;m()(v,"components",{QTable:g["a"],QTd:h["a"]})},b777:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"q-pa-md"},[a("div",{staticClass:"q-gutter-y-md"},[a("q-tab-panels",{staticClass:"shadow-2 rounded-borders",attrs:{animated:""},model:{value:e.panel,callback:function(t){e.panel=t},expression:"panel"}},[a("q-tab-panel",{attrs:{name:"locus_tag"}},[a("div",{staticClass:"text-h5"},[e._v(e._s(this.$route.params.code))]),a("q-badge",{attrs:{color:"purple"}},[e._v("Cyanobacteria")])],1)],1),a("q-card",[a("q-tabs",{staticClass:"text-grey",attrs:{dense:"","active-color":"primary","indicator-color":"primary",align:"justify","narrow-indicator":""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[a("q-tab",{attrs:{name:"base",label:"Base Information"}}),a("q-tab",{attrs:{name:"environment",label:"Environment"}}),a("q-tab",{attrs:{name:"jbrowse",label:"JBrowse"}})],1),a("q-separator"),a("q-tab-panels",{attrs:{animated:""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[a("q-tab-panel",{attrs:{name:"base"}},[a("base-data")],1),a("q-tab-panel",{attrs:{name:"environment"}},[a("environment")],1),a("q-tab-panel",{attrs:{name:"jbrowse"}},[a("jbrowse")],1)],1)],1)],1)])},r=[],o=(a("9f3c"),a("a70f")),i=a("bd26"),c=a("0e52"),s={name:"detail",data:function(){return{tab:"base",panel:"locus_tag"}},components:{"base-data":o["default"],environment:i["default"],jbrowse:c["default"]}},l=s,d=a("2877"),u=a("eebe"),b=a.n(u),p=a("adad"),f=a("823b"),m=a("58a8"),g=a("f09f"),h=a("429b"),v=a("7460"),y=a("eb85"),_=Object(d["a"])(l,n,r,!1,null,"b9b85248",null);t["default"]=_.exports;b()(_,"components",{QTabPanels:p["a"],QTabPanel:f["a"],QBadge:m["a"],QCard:g["a"],QTabs:h["a"],QTab:v["a"],QSeparator:y["a"]})},bd26:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"q-pa-md"},[a("q-table",{attrs:{title:e.code,data:e.data,columns:e.columns,"row-key":"condition",separator:"cell",pagination:e.pagination},on:{"update:pagination":function(t){e.pagination=t}},scopedSlots:e._u([{key:"body-cell-condition",fn:function(t){return[a("q-td",{attrs:{props:t}},[a("q-badge",{attrs:{color:"purple"}},[e._v("\n            "+e._s(t.value)+"\n          ")])],1)]}}])})],1),a("div",{staticClass:"q-pa-md"},[a("q-tab-panel",{staticClass:"shadow-4"},[a("div",{staticClass:"text-h6"},[e._v(e._s("Difference analysis of "+this.$route.params.code))]),a("q-separator"),a("q-img",{staticStyle:{width:"80%",height:"80%"},attrs:{src:e.img_url}})],1)],1)])},r=[],o=a("9f3c"),i={name:"environment",data:function(){return{img_url:null,pagination:{page:1,rowsPerPage:10},code:null,columns:[{name:"condition",field:"condition",align:"center",label:"condition",sortable:!0},{name:"padj",field:"padj",align:"center",label:"padj",sortable:!0},{name:"log2",field:"log2",align:"center",label:"log2FoldChange",sortable:!0}],data:[]}},mounted:function(){var e=this;this.code="Controlled experiment with ".concat(this.$route.params.code),o["a"].search_environment({q:this.$route.params.code},(function(t){"success"===t.data.code?t.data.data===[]?e.$q.notify({message:"Please Refresh!"}):e.data=t.data.data:e.$q.notify({message:"Error! Try again"})})),o["a"].environment_image({q:this.$route.params.code},(function(t){"success"===t.data.code?e.img_url=t.data.data.img_url:e.$q.notify({message:"Error! Try again"})}))}},c=i,s=a("2877"),l=a("eebe"),d=a.n(l),u=a("eaac"),b=a("db86"),p=a("58a8"),f=a("823b"),m=a("eb85"),g=a("068f"),h=Object(s["a"])(c,n,r,!1,null,"3b466b1d",null);t["default"]=h.exports;d()(h,"components",{QTable:u["a"],QTd:b["a"],QBadge:p["a"],QTabPanel:f["a"],QSeparator:m["a"],QImg:g["a"]})}}]);