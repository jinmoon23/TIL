<template>
  <div>
    <h1>ArticleView 페이지 입니다.</h1>
    <!-- create 기능 구현 -->
    <RouterLink :to="{name:'CreateView'}">Create</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
// import { onMounted } from 'vue'
// import { useArticleStore } from '@/stores/counter';
import { RouterLink } from 'vue-router';
// const store = useArticleStore()
// onMounted(() => {
//   // mount 되기 전에 store에 있는 전체 게시글 요청 함수를
//   // 호출 해야함.
//   store.getArticles()
//   // 근데 왜 error가 발생하지??
//   // 그것은 CORS 정책과 관련됨
// })
</script>

<style>

</style>
