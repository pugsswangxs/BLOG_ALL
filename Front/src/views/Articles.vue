<template>
  <div class="articles">
    <banner></banner>
    <div class="site-content animate">

      <main class="site-main">
        <article class="hentry">
          <!-- 文章头部 -->
          <header class="entry-header">
            <!-- 标题输出 -->
            <h1 class="entry-title">{{ postdetail.title }}</h1>
            <hr>
            <div class="breadcrumbs">
              <div id="crumbs">{{ postdetail.pubTime }}</div>
            </div>
          </header>
          <!-- 正文输出 -->
          <div class="entry-content" v-highlight v-html="article" id="content">
          </div>
          <!-- 文章底部 -->
          <section-title>
            <footer class="post-footer">
              <!-- 阅读次数 -->
              <div class="post-like">
                <i class="iconfont iconeyes"></i>
                <span class="count">{{ postdetail.viewsCount }}</span>
              </div>
              <div class="donate" @click="showDonate=!showDonate">
                <span>赏</span>
                <!--                                <ul class="donate_inner" :class="{'show':showDonate}">-->
                <!--                                    <li class="wedonate"><img src="http://cdn.fengziy.cn/gblog/wexin_pay.png"><p>微信</p></li>-->
                <!--                                    <li class="alidonate"><img src="http://cdn.fengziy.cn/gblog/ali_pay.jpg"><p>支付宝</p></li>-->
                <!--                                </ul>-->
              </div>
              <!-- 文章标签 -->
              <div class="post-tags">
                <i class="iconfont iconcategory"></i>
                <router-link v-for="item in postdetail.tags" :key="item.id"
                             :to="{ name: 'tag', params: { tag: item.tag }}">{{ item.tag }}&nbsp;
                </router-link>
              </div>
            </footer>
          </section-title>

          <!--声明-->
          <div class="open-message">
            <p>声明：|版权所有，违者必究|如未注明，均为原创|本网站感谢 <a href="https://gitee.com/xiejava" target="_blank">xiejava
              大佬</a>gitee上的代码支持</p>
            <p>转载：转载请注明原文链接 - <a href="/">{{ postdetail.title }}</a></p>
          </div>
          <!--评论-->
          <div class="comments">
            <comment v-for="item in comments" :key="item.comment.id" :comment="item.comment">
              <template v-if="item.reply.length">
                <comment v-for="reply in item.reply" :key="reply.id" :comment="reply"></comment>
              </template>
            </comment>
          </div>
        </article>
      </main>
      <!-- 文章目录 -->
      <section class="right-side">
        <div id="article-menus">
          <menu-tree :menus="menus" child-label="child"></menu-tree>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import Banner from '@/components/banner'
import sectionTitle from '@/components/section-title'
import comment from '@/components/comment'
import menuTree from '@/components/menu-tree'
import {fetchComment, fetchPostDetail} from '../api'
// 将marked 引入
import {marked} from 'marked';

export default {
  name: 'articles',
  data() {
    return {
      showDonate: false,
      comments: [],
      menus: [],
      postdetail: {},
      article: ''
    }
  },
  components: {
    Banner,
    sectionTitle,
    comment,
    menuTree,
  },
  computed: {
    id() {
      return this.$route.params.id
    }
  },
  methods: {
    getPostDetail() {
      console.log('getPostDetail()' + this.id)
      fetchPostDetail(this.id).then(res => {
        this.postdetail = res.data
        // 调用marked()方法，将markdown转换成html
        this.article = marked(this.postdetail.content);
        console.log(res.data)
        this.$nextTick(function () {
          console.log('开始构建菜单')
          this.createMenus()
        })
      }).catch(err => {
        console.log(err)
      })

    },
    getComment() {
      fetchComment().then(res => {
        this.comments = res.data || []
      }).catch(err => {
        console.log(err)
      })
    },
    fetchH(arr, left, right) {
      if (right) {
        return arr.filter(item => item.offsetTop > left && item.offsetTop < right)
      } else {
        return arr.filter(item => item.offsetTop > left)
      }
    },
    // 生成目录
    createMenus() {
      let arr = []
      for (let i = 6; i > 0; i--) {
        let temp = []
        let e = document.querySelector(".entry-content").querySelectorAll(`h${i}`)
        for (let j = 0; j < e.length; j++) {
          let child = this.fetchH(arr, e[j].offsetTop, (j + 1 === e.length) ? undefined : e[j + 1].offsetTop)
          temp.push({
            h: i,
            title: e[j].innerText,
            id: e[j].id,
            offsetTop: e[j].offsetTop,
            child
          })
        }
        if (temp.length) {
          arr = temp
        }
      }
      this.menus = arr
      console.log('this.menus---')
      console.log(this.menus)
    }
  },
  mounted() {
    this.createMenus()
  },
  created() {
    //this.getComment()
    this.getPostDetail()
  },
}
</script>
<style scoped lang="less">
.site-content {
  display: flex;
  position: relative;
  max-width: 800px;

.site-main {
  padding: 80px 0 0 0;
  max-width: 800px;
}

}
#article-menus {
  position: sticky;
  top: 0;
  box-shadow: 0 2px 6px rgba(0, 0, 0, .1);
  border-radius: 3px;
  padding: 15px;
  width: 300px;
  transform: translateY(150px);
  font-size: 14px;
}

.right-side {
  margin-left: 30px;
}

article.hentry {

.entry-header {

.entry-title {
  font-size: 30px;
  font-weight: 600;
  color: #2B2B2B;
  margin: 0.67em 0;

&
:before {
  /*content: "#";*/
  margin-right: 6px;
  color: #d82e16;
  font-size: 20px;
  font-weight: 600;
}

}

hr {
  height: 1px;
  border: 0;
  background: #EFEFEF;
  margin: 15px 0;
}

.breadcrumbs {
  font-size: 14px;
  color: #D2D2D2;
  text-decoration: none;
  margin-bottom: 30px;
}

}

.entry-content {

}

footer.post-footer {
  width: 100%;
  padding: 20px 10px;
  margin-top: 30px;
  height: 65px;
  position: relative;

i {
  font-size: 18px;
  margin-right: 5px;
}

.post-like {
  float: right;
  margin: 7px 0 0 20px;
}

.post-share {
  float: right;
  list-style: none;
  margin-right: 20px;
}

.donate {
  float: left;
  line-height: 36px;
  border-radius: 100%;
  -webkit-border-radius: 100%;
  -moz-border-radius: 100%;
  border: 1px solid #2B2B2B;

&
:hover {
  border: 1px solid goldenrod;

span {
  color: goldenrod;
}

}
span {
  color: #2B2B2B;
  padding: 10px;
  position: relative;
  cursor: pointer;
}

.donate_inner {
  display: none;
  margin: 0;
  list-style: none;
  position: absolute;
  left: 80px;
  top: -40px;
  background: #FFF;
  padding: 10px;
  border: 1px solid #ddd;
  box-shadow: 0 2px 6px rgba(0, 0, 0, .08);
  border-radius: 3px;

&
.show {
  display: block;
}

li {
  float: left;
}

img {
  width: 100px;
}

p {
  text-align: center;
  font-size: 15px;
  color: #D2D2D2;
  line-height: 1rem;
}

}

.donate_inner:after, .donate_inner:before {
  content: "";
  position: absolute;
  left: 0;
  bottom: 45%;
  margin-left: -8px;
  border-top: 8px solid transparent;
  border-bottom: 8px solid transparent;
  border-right: 8px solid #fff;
}

.donate_inner:before {
  left: -1px;
  border-right: 8px solid #ddd;
}

}

.post-tags {
  margin: 7px 0 0 20px;
  float: left;
  text-transform: uppercase;

a:hover {
  color: #ff6d6d;
}

}
}
.open-message {
  margin: 50px 0;
  position: relative;
  background: #2B2B2B;
  padding: 10px 30px;
  border-radius: 3px;
  font-size: 14px;
  color: #fff;

&
:after {
  content: "";
  border-left: 10px solid transparent;
  border-right: 10px solid transparent;
  border-bottom: 10px solid #2B2B2B;
  position: absolute;
  top: -8px;
  left: 48%;
}

p {
  margin: 10px 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

a {
  color: #A0DAD0;
  padding: 0 5px;
}

}
}

@media (max-width: 1490px) {
  #article-menus {
    display: none;
  }

  .right-side {
    display: none;
  }
}

@media (max-width: 800px) {
  #article-menus {
    display: none;
  }
}

@media (max-width: 1600px) {
  .right-side {
    margin-left: 30px;
  }
}

</style>
