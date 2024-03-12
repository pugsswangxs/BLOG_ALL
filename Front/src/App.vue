<template>
    <div id="app" v-cloak>
        <loading></loading>
        <layout-header></layout-header>
        <layout-body></layout-body>
        <layout-footer></layout-footer>
    </div>
</template>
<script>
    import layoutHeader from '@/components/layout/layout-header'
    import layoutBody from '@/components/layout/layout-body'
    import layoutFooter from '@/components/layout/layout-footer'
    import Loading from '@/components/loading'
    export default {
        name: "app",
        components: {
            layoutHeader,
            layoutBody,
            layoutFooter,
            Loading
        }
    }
</script>
<style lang="less">
    #app {
        font-size: 17px;
        color: #6f6f6f;
        padding-top: 40px;
  background-image: url('https://img.zcool.cn/community/038858d5785bd5d0000018c1bdc52e5.jpg');
  background-size: cover; /* 根据需要调整背景图片的大小 */
  background-position: center; /* 背景图片的位置 */
  background-repeat: no-repeat; /* 不重复背景图片 */
    }
</style>
