import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const usePostStore = defineStore('post', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const posts = ref([])
  const getPosts = function () {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/posts/`
    })
    .then((response) => {
      console.log(response)
      posts.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return {
    API_URL,
    posts,
    getPosts
  }
})
