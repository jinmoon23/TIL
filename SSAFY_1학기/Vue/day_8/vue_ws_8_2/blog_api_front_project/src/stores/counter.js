import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const usePostStore = defineStore('post', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const posts = ref([])
  const categories = ref([])
  const router = useRouter()
  const getPosts = function () {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/posts/`
    })
    .then((response) => {
      posts.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const getCategories = function () {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/categories/`
    })
    .then((response) => {
      categories.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const createCategory = function (payLoad) {
    const {name} = payLoad
    axios({
      method: 'post',
      url: `${API_URL}/api/v1/categories/`,
      data: {
        name
      }
    })
    .then((response) => {
      router.push({name:'main'})
      console.log('카테고리 저장 완료')
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return {
    API_URL,
    posts,
    getPosts,
    categories,
    getCategories,
    createCategory
  }
})
