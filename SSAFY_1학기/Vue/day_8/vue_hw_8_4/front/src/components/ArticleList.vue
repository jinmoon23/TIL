<template>
  <div>
    <RouterLink :to="{name:'create'}">게시글 생성</RouterLink>
    <ArticleListItem 
      v-for="article in store.articles"
      :article="article"
    />
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useArticleStore } from '@/stores/articles'
import ArticleListItem from '@/components/ArticleListItem.vue';
const store = useArticleStore()
// 아래와 같이 구성한 후 위에서 반복 돌리면 참조가 누락되는
// 경우가 발생할 수 있음. 따라서 곧바로 넘겨주는게 더 낫다.
// const articleList = store.articles
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>

</style>