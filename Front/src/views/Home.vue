<template>
  <div class="home">
    <banner isHome="true"></banner>
    <div class="site-content">
      <!--通知栏-->
      <div class="notify">
        <div class="search-result" v-if="hideSlogan">
          <span v-if="searchWords">搜索结果："{{ searchWords }}" 相关文章</span>
          <span v-else-if="category"><img :src="srcimg" width="300" height="200">分类 "{{ selectType }}" 相关文章</span>
          <span v-else-if="searchTag">标签 "{{ searchTag }}" 相关文章</span>
        </div>

        <quote v-else>{{ notice }}</quote>
      </div>

      <!--标签-->
      <div v-if="!hideSlogan">
        <el-card style="width: auto;">
          <div slot="header" class="card-header" >可选择标签列表</div>
          <div class="tag-group" style="
          display: flex;
          flex-wrap: wrap;
          align-items: center;
          justify-content: flex-start;
          gap: 5px;">
            <el-button v-for="(item, index) in tags" :key="item.tag"
                       :style="{ backgroundColor: generateRandomColor() ,
                                color: '#000',
                                fontWeight: 'bold' }">
              <router-link :to="`/tag/${item.tag}`">{{ item.tag }}</router-link>
            </el-button>
          </div>
        </el-card>
      </div>

      <!--文章列表-->
      <main class="site-main" :class="{'search':hideSlogan}">
        <section-title v-if="!hideSlogan">推荐</section-title>
        <template v-for="item in postList">
          <post :post="item" :key="item.id"></post>
        </template>
      </main>

      <!--加载更多-->
      <div class="more" v-show="hasNextPage">
        <div class="more-btn" @click="loadMore">More</div>
      </div>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/banner'
import Feature from '@/components/feature'
import sectionTitle from '@/components/section-title'
import Post from '@/components/post'
import SmallIco from '@/components/small-ico'
import Quote from '@/components/quote'
import {fetchCategory, fetchFocus, fetchList, fetchTags} from '../api'

export default {
  name: 'Home',
  props: ['cate', 'words', 'tag'],
  data() {
    return {
      features: [],
      postList: [],
      currPage: 1,
      hasNextPage: false,
      catedatadict: {},
      selectType: '',
      srcimg: '',
      tags: []
    }
  },
  components: {
    Banner,
    Feature,
    sectionTitle,
    Post,
    SmallIco,
    Quote
  },
  computed: {
    searchWords() {
      return this.$route.params.words
    },
    category() {
      return this.$route.params.cate
    },
    searchTag() {
      return this.$route.params.tag
    },
    hideSlogan() {
      this.selectType = this.category || this.searchWords || this.searchTag
      return this.selectType
    },
    notice() {
      return this.$store.getters.notice
    },

  },
  watch: {
    $route() {
      console.log('--watch.route()')
      //调用路由后的其他方法
      this.fetchList();
      this.GetCatePng();
    }
  },
  methods: {
    fetchFocus() {
      fetchFocus().then(res => {
        this.features = res.data || []
      }).catch(err => {
        console.log(err)
      })
    },
    fetchList() {
      fetchList({words: this.searchWords, cate: this.category, tag: this.searchTag}).then(res => {
        this.postList = res.data.items || []
        this.currPage = res.data.page
        this.hasNextPage = res.data.hasNextPage
      }).catch(err => {
        console.log(err)
      })
    },
    loadMore() {
      fetchList({page: this.currPage + 1}).then(res => {
        this.postList = this.postList.concat(res.data.items || [])
        this.currPage = res.data.page
        this.hasNextPage = res.data.hasNextPage
      })
    },
    GetCatePng() {
      fetchCategory().then(res => {
            res.data.forEach(item => {
              this.catedatadict[item.title] = item.href;
            });
            this.srcimg = this.catedatadict[this.selectType];
          }
      ).catch(err => {
        console.log(err)
      })

    },
    fetchTags() {
      fetchTags().then(res => {
        this.tags = res
      }).catch(err => {
        console.log(err)
      })
    },
    generateRandomColor() {
      return '#' + ((Math.random() * 0xFFFFFF << 0).toString(16)).padStart(6, '0');
    },

  },
  mounted() {
    this.fetchFocus();
    this.fetchList();
    this.GetCatePng();
    this.fetchTags();
  },
  created() {
    // await this.GetCatePng()
    // console.log('--created()')
    // this.fetchFocus();
    // this.fetchList();

  }
}
</script>
<style scoped lang="less">

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  background-color: #f5f7fa; /* 背景色 */
  font-size: 18px; /* 字体大小 */
  font-weight: bold; /* 字体加粗 */
  color: #303133; /* 文字颜色 */
  border-bottom: 1px solid #ebeef5; /* 下边框 */
}

.site-content {

.notify {
  margin: 60px 0;
  border-radius: 3px;

&
> div {
  padding: 20px;
}

}


.search-result {
  padding: 15px 20px;
  text-align: center;
  font-size: 20px;
  font-weight: 400;
  border: 1px dashed #ddd;
  color: #828282;
}

}


.top-feature {
  width: 100%;
  height: auto;
  margin-top: 30px;

.feature-content {
  margin-top: 10px;
  display: flex;
  justify-content: space-between;
  position: relative;

.feature-item {
  width: 32.9%;
}

}
}

.site-main {
  padding-top: 80px;

&
.search {
  padding-top: 0;
}

}

.more {
  margin: 50px 0;

.more-btn {
  width: 100px;
  height: 40px;
  line-height: 40px;
  text-align: center;
  color: #ADADAD;
  border: 1px solid #ADADAD;
  border-radius: 20px;
  margin: 0 auto;
  cursor: pointer;

&
:hover {
  color: #8fd0cc;
  border: 1px dashed #8fd0cc;
}

}
}

/******/
@media (max-width: 800px) {
  .top-feature {
    display: none;
  }

  .site-main {
    padding-top: 40px;
  }

  .site-content {

  .notify {
    margin: 30px 0 0 0;
  }

  .search-result {
    margin-bottom: 20px;
    font-size: 16px;
  }
}

}

/******/
</style>
