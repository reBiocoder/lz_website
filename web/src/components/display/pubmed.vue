<template>
  <div class="q-pa-md">
    <q-tab-panel class="shadow-4" name="pubmed">
      <q-input
        v-model="search"
        debounce="500"
        filled
        placeholder="Please enter keywords and search in pubmed"
        @keyup.enter="getPubmed(search)"
      >
        <template v-slot:append>
          <q-icon @click="getPubmed(search)" name="search"/>
        </template>
      </q-input>
      <q-card flat bordered v-if="dataCount===0">
        <q-card-section>
         <q-skeleton type="rect"/>
        </q-card-section>

        <q-separator/>

        <q-card-section>
          <q-skeleton type="QToolbar"/>
        </q-card-section>
      </q-card>
      <div v-if="dataCount !==0">{{`Pubmed finds about ${dataCount} related results for you`}}</div>
      <q-list bordered separator>
        <div>
          <div v-if="dataCount !==0">
            <article class="labs-full-docsum"
                     v-for="(eachList,index) in dataList.slice((currentPage-1)*pagesize,currentPage*pagesize)">

              <div class="selector-wrap first-selector">
                <label class="search-result-position"><span
                  class="position-number">{{index+1+(currentPage-1)*pagesize}}</span></label>
              </div>
              <div class="docsum-wrap">
                <div class="docsum-content">
                  <div class="docsum-add">
                    <a style="text-decoration:none;" class="labs-docsum-title"
                       v-bind:href="'https://pubmed.ncbi.nlm.nih.gov/?term='+eachList.pmid"
                       data-ga-category="result_click" data-ga-action="1" data-ga-label="28472718">
                      {{ eachList.title }}
                    </a>
                  </div>
                  <div class="labs-docsum-citation">
                    {{eachList.authorLastName}} {{eachList.authorInitial}}, et al. {{eachList.medlineTA}}
                    {{eachList.pubdate}}
                    - DOI <span class="docsum-pmid"><a style="text-decoration:none;"
                                                       :href="'https://doi.org/'+eachList.doi">{{eachList.doi}}</a></span>.
                    PMID <span class="docsum-pmid"><a style="text-decoration:none;"
                                                      v-bind:href="'https://pubmed.ncbi.nlm.nih.gov/?term='+eachList.pmid">{{eachList.pmid}}</a></span>
                  </div>
                  <div class="labs-docsum-snippet">
                    <div class="full-view-snippet">
                      {{eachList.abstract}}
                      …
                    </div>
                  </div>
                </div>
              </div>
            </article>
            <q-pagination
              v-model="currentPage"
              :max="maxPage"
              :direction-links="true"
              v-if="dataCount !== 0"
            >
            </q-pagination>
          </div>
        </div>

      </q-list>
    </q-tab-panel>
  </div>
</template>

<script>
  import http from '../../api/display'

  export default {
    name: "pubmed",
    data() {
      return {
        search: "",
        currentPage: 1,
        pagesize: 25,
        dataCount: 0,
        current: 1,
        dataList: [],
        maxPage: 1,
      }
    },
    methods: {
      getPubmed(keyword) {
        this.dataCount = 0  // 返回初始状态
        http.pubmed({"q": keyword}, (res) => {
          if (res.data.code === 'success') {
            this.dataList = res.data.data.result
            this.dataCount = res.data.data.count
            this.maxPage = Math.ceil(this.dataCount / 25)
          } else {
            this.$q.notify({
              message: res.data.info
            })
          }
        })
      }
    },
    mounted() {
      this.getPubmed('Cyanobacteria')
    }
  }
</script>

<style scoped>
  .labs-full-docsum {
    padding: 0;
    position: relative;
    margin-bottom: 20px;
  }

  .docsum-add a {
    font-size: 18px;
    color: #205493;
  }

  .labs-full-docsum > .selector-wrap {
    display: inline-block;
    padding-right: 1.6rem;
    padding-left: 1px;
    vertical-align: top;
    color: #5b616b;
  }

  .labs-full-docsum .docsum-wrap {
    display: inline-block;
    width: 90%;
  }

  .labs-full-docsum .result-actions-bar {
    margin-top: .6rem;
    display: block;
  }

  .labs-full-docsum .labs-docsum-title {
    display: inline-block;
    outline-offset: 0;
    word-wrap: break-word;
    width: 100%;
  }

  .labs-full-docsum .labs-docsum-citation {
    color: #2e8540;
  }

  .labs-full-docsum .labs-docsum-citation a {
    color: #2e8540;
  }

  .labs-full-docsum .labs-docsum-snippet {
    line-height: 1.8rem;
    font-size: 14px;
    color: #212121;
  }

  .labs-full-docsum .labs-docsum-snippet .full-view-snippet {
    display: block;
  }

  .labs-full-docsum .labs-docsum-snippet .short-view-snippet, .search-results-chunk .labs-full-docsum .labs-docsum-snippet .full-view-snippet {
    display: none;
  }

  .labs-full-docsum .result-actions-bar {
    margin-top: .6rem;
    display: block;
  }

  .labs-full-docsum .result-actions-bar .cite {
    display: inline-block;
  }

  .labs-full-docsum .result-actions-bar .share {
    display: inline-block;
  }

  .demo-form-inline {
    display: inline-block;
  }
</style>
