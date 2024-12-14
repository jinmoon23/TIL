import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useArticleStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL= 'http://127.0.0.1:8000'
  // 1. DRF로 전체 게시글 요청을 보내고 응답을 받아
  // articles에 저장하는 함수를 정의
  // 해당 함수는 비동기로 동작하기 때문에 사용자 경험을 위해
  // 미리 호출해야 함! 따라서 onMounted를 활용하면 좋다.
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
    })
    .then((response) => {
      // console.log(response)
      // console.log(response.data)
      // django로부터 받아온 데이터를 기반으로 articles 배열을 채움
      // 성공적인 첫 소통!
      articles.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return {
    articles,
    API_URL,
    getArticles
  }
}, { persist: true })
