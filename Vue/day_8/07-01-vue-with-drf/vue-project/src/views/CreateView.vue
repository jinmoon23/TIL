<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <div>
        <label for="title">제목</label>
        <input type="text" id="title" v-model.trim="titleInput"> 
      </div>
      <div>
        <label for="content">내용</label>
        <textarea id="content" v-model.trim="contentInput"></textarea>
      </div>
      <input type="submit" value="작성하기">
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useArticleStore } from '@/stores/counter';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useArticleStore()
// 양방향 바인딩 설정
const titleInput = ref('')
const contentInput = ref('')

const createArticle = function () {
  axios({
    method:'post',
    url: `${store.API_URL}/api/v1/articles/`,
    // post 데이터 요청시 필요한 키값쌍!
    data:{
      title: titleInput.value,
      content: contentInput.value
    }
  })
  .then((response) => {
    console.log('저장 성공')
    router.push({name:'ArticleView'})
  })
  .catch((error) => {
    console.log(error)
  })
}

</script>

<style>

</style>
