(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[17],{dfbe:function(e,t,a){"use strict";a.r(t);var n=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("div",{staticClass:"q-pa-md"},[a("q-table",{attrs:{data:e.data,columns:e.columns,separator:e.separator,pagination:e.pagination,"rows-per-page-options":[50,200,500,1e3,0],filter:e.filter},on:{"update:pagination":function(t){e.pagination=t}},scopedSlots:e._u([{key:"top-left",fn:function(){return[a("div",{staticClass:"text-purple text-h6"},[e._v("626 complete or draft genomic data of cyanobacteria are included!")])]},proxy:!0},{key:"top-right",fn:function(){return[a("q-input",{attrs:{borderless:"",dense:"",debounce:"300",color:"primary",label:"Search for expect species"},scopedSlots:e._u([{key:"append",fn:function(){return[a("q-icon",{attrs:{name:"search"}})]},proxy:!0}]),model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}})]},proxy:!0},{key:"header",fn:function(t){return[a("q-tr",{attrs:{props:t}},e._l(t.cols,(function(n){return a("q-th",{key:n.name,attrs:{props:t}},[e._v("\n              "+e._s(n.label)+"\n")])})),1)]}},{key:"body-cell-RefSeq_assm_no",fn:function(t){return[a("q-td",{attrs:{props:t}},[a("div",[a("router-link",{staticStyle:{"text-decoration":"none"},attrs:{to:{name:"cyano",params:{code:t.row.RefSeq_assm_no}}}},[e._v("\n                "+e._s(t.row.RefSeq_assm_no)+"\n              ")])],1)])]}}])})],1)])},o=[],r=a("9f3c"),s=a("c9d9"),i={name:"index",data:function(){return{filter:null,pagination:{page:1,rowsPerPage:50},separator:"horizontal",columns:[],data:[]}},method:{},components:{},mounted:function(){var e=this;r["a"].get_cyano_genomes((function(t){if("success"===t.data.code){for(var a=t.data.data.header,n=[],o=0,r=a.length;o<r;++o)n.push({name:a[o],label:Object(s["b"])(a[o]),align:"center",field:a[o],sortable:!0});e.columns=n,e.data=t.data.data.data}else e.$q.notify({message:t.data.info})}))}},c=i,l=a("2877"),p=a("eaac"),d=a("27f9"),u=a("0016"),f=a("bd08"),m=a("357e"),b=a("05c0"),_=a("db86"),y=a("eebe"),g=a.n(y),h=Object(l["a"])(c,n,o,!1,null,"4210252a",null);t["default"]=h.exports;g()(h,"components",{QTable:p["a"],QInput:d["a"],QIcon:u["a"],QTr:f["a"],QTh:m["a"],QTooltip:b["a"],QTd:_["a"]})}}]);