<template>
  <div class="about" style="background: https://img.zcool.cn/community/038858d5785bd5d0000018c1bdc52e5.jpg">
    <div class="site-content">
      <div class="content-warp">

        <div class="about-site about-info">
          <el-card>
            <el-divider content-position="left">
              <span style="font-family: Arial; color: ; font-size: 20px;">关于本人</span>
              <span>❤</span></el-divider>
            <div class="info-card">
              <p>偶然之间看见了<a target="_blank" class="out-link" href="https://zhebk.cn/Web/Akina.html">Akina For
                Typecho</a>博客的主题，风格很是喜欢。</p>
              <p>然后就开始用Vue搭建这种风格的博客，在此呢也将这套模板开放给大家。</p>
              <p><a target="_blank" href="https://gitee.com/fengziy/Gblog" style="color: #ff6d6d;">Gitee仓库</a> | <a
                  target="_blank" href="https://github.com/fengziye/Gblog" style="color: #ff6d6d;">Github仓库</a>记得star★哟
              </p>
            </div>
            <el-divider content-position="left">
              <span style="font-family: Arial; color: ; font-size: 20px;">关于博客</span>
              <span>❤</span></el-divider>
            <div class="info-card">
              <p style="text-indent:2em">一直想通过VUE+DJANGO 搭建自己的网站。但是一直没有时间自己去搭建，也没有找到合适的模板。后来看到
                <a target="_blank" href="https://gitee.com/fengziy/Gblog" style="color: #ff6d6d;">fengziy</a>
                大佬的文章，觉得他的博客风格很是喜欢。 于是就在此基础上进行了与完善，最终完成了本站的制作。</p>
              <el-divider></el-divider>

              <p>完善后的本站的前后端的github路径如下:</p>
              <p><a target="_blank" href="https://github.com/pugsswangxisnheng/BLOG_ALL"
                    style="color: #ff6d6d;background-color: #4a86e8;">Pugss
                Github仓库</a>  方便的话记得给个star★哟
              </p>
              <el-divider></el-divider>
              <p>fengziy 大佬的github路径如下:</p>
              <p><a target="_blank" href="https://github.com/fengziye/Gblog" style="color: #ff6d6d;">fengziye
                Github仓库</a>记得star★哟
              </p>
            </div>
          </el-card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import sectionTitle from '@/components/section-title'
import {getTime, getTimeInterval} from '@/utils'
// import Quote from "@/components/quote";
// import {fetchFriend} from '../api'
export default {
  name: "About",
  data() {
    return {
      list: []
    }
  },
  components: {
    // Quote,
    sectionTitle
  },
  methods: {},
  mounted() {
  }
}
</script>
<style scoped lang="less">
.about {
  padding-top: 40px;
  background-image: url('http://47.102.156.92:3080/other/site_background.jpg');
  background-size: cover; /* 根据需要调整背景图片的大小 */
  background-position: center; /* 背景图片的位置 */
  background-repeat: no-repeat; /* 不重复背景图片 */
}
.content-warp {
  margin-top: 80px;

.about-info {
  margin: 30px 0;

span {
  color: red;
  margin-right: 10px;
}

.info-card {
  min-height: 100px;
  padding: 20px;
  border-radius: 3px;
  margin: 30px 0 50px 0;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

p {
  line-height: 1.7rem;
}

}
}

.contactForm {
  width: 100%;
  padding: 20px;

.form-item {
  align-items: center;
  display: flex;

&
:not(:last-child) {
  margin-bottom: 20px;
}

label {
  width: 80px;
}

.v {
  min-height: 40px;
  line-height: 20px;
  border-radius: 3px;
  padding: 2px 10px;
  outline: none;
  border: 1px solid #8fd0cc;
  width: 100%;
  resize: vertical;
}

button {
  width: 100px;
  height: 40px;
  border-radius: 3px;
  outline: 0;
  border-style: none;
  cursor: pointer;
  background-color: #409eff;
  color: white;

&
:hover {
  opacity: 0.8;
}

}
}
}
}

/*******/
@media (max-width: 800px) {
  .content-warp {
    margin-top: 0;
  }
}
</style>
