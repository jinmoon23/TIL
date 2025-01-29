<template>
    <div>
      <h1>게시글 생성하기</h1>
      <form @submit.prevent="createArticle">
        <label for="title">제목</label>
        <input type="text" id="title" v-model="titleInput">
        <label for="content">내용</label>
        <textarea id="content" v-model="contentInput"></textarea>
        <input type="submit" value="생성하기">
      </form>
    </div>
</template>

<script setup>
import axios from 'axios'
import {ref} from 'vue'
import { useArticleStore } from '@/stores/articles';
import { useRouter } from 'vue-router';
const router = useRouter()
const store = useArticleStore()
// 1. 양방향 바인딩
const titleInput = ref('')
const contentInput = ref('')
// 2. store의 articles 배열에 추가하는 함수
// axios POST 요청을 통해 저장하기
const createArticle = function () {
  axios({
    method:'post',
    url: `${store.API_URL}/api/v1/articles/`,
    // 3. post 요청을 하는 경우 필수적인 키값쌍!!
    data:{
      title: titleInput.value,
      content: contentInput.value
    }
  })
  .then((response) => {
    console.log('저장 성공')
    // 4. create 완료 후 list 페이지로 이동하는 기능 구현
    router.push({name:'home'})
  })
  .catch((error) => {
    console.log(error)
  })
}

</script>

<style scoped>

</style>
