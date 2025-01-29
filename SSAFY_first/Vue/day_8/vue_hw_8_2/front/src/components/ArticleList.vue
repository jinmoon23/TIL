<template>
  <div>
    
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()
const articleList = store.articles
onMounted(() => {
  store.getArticles()
})
</script>

<style lang="scss" scoped>

</style>