import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useTodoStore = defineStore('todo', () => {
  const todos = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getTodos = function () {
    axios({
      method:'get',
      url:`${API_URL}/api/v1/todos/`
    })
    .then((response) => {
      console.log(response)
      todos.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  return {
    todos,
    API_URL,
    getTodos
  }
}, { persist: true })
