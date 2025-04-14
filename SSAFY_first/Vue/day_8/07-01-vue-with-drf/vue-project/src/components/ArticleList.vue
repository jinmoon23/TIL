<template>
  <div>
    <h3>Article List 페이지 입니다.</h3>
    <ArticleListItem 
      v-for="article in articleList"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>

import ArticleListItem from '@/components/ArticleListItem.vue'
import { useArticleStore } from '@/stores/counter'
import { onMounted } from 'vue'
const store = useArticleStore()
const articleList = store.articles
// 일단은 articleView와 여기 list 어디에서 호출하든 상관없이 동작함
// 추측하기로 데이터의 양이 얼마 없어서 그런거 같음.
onMounted( () => {
  store.getArticles()
})
</script>
