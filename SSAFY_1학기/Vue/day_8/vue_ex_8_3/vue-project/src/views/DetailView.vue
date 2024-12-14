<template>
    <div v-if="todo"> 
      <h1>TodoDetailView</h1>
      <p>할 일 번호: {{ todo.id }}</p>
      <p>할 일 제목: {{ todo.work }}</p>
      <p>할 일 내용: {{ todo.content }}</p>
      <p>할 일 상태: {{ todo.is_completed }}</p>
      <p>할 일 생성일: {{ todo.created_at }}</p>
    </div>
</template>

<script setup>
import axios from 'axios';
import { useRoute } from 'vue-router';
import { useTodoStore } from '@/stores/todoStore';
import { onMounted, ref} from 'vue';
const route = useRoute()
const store = useTodoStore()

const todoId = route.params.id
const todo = ref({})
onMounted(() => {
  axios({
    method:'get',
    url:`${store.BASE_URL}/api/v1/todos/${todoId}/`
  })
  .then((response) => {
    todo.value = response.data
  })
  .catch((error) => {
    console.log(error)
  })
})
</script>

<style scoped>

</style>