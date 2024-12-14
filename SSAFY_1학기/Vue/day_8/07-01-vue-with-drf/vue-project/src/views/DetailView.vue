<template>
  <div v-if="article">
    <h1>DetailView 페이지 입니다.</h1>
    게시물 ID: {{ article.id }} <br>
    {{ article.title }} <br>
    {{ article.content }}
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted , ref} from 'vue';
import { useArticleStore } from '@/stores/counter';
import { useRoute } from 'vue-router';
const store = useArticleStore()
const route = useRoute()
const articleId = route.params.id
// {} 또는 null로 해도 됨.
const article = ref({})
// DetailView가 mount되기 전에 django로 응답 데이터(단일 게시글)를 받은 후
// 해당 페이지를 보여줘야 함.
onMounted(() => {
  axios({
    method:'get',
    url: `${store.API_URL}/api/v1/articles/${articleId}`,
  })
  .then((response) => {
    console.log(response)
    article.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
})
</script>

<style>

</style>
