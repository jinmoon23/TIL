<template>
<main>
  <h1>할 일 목록</h1>
  <ul v-for="todo in todos" :key="todo.id">
    title: {{ todo.work }} <br>
    content: {{ todo.content }}
  </ul>
</main>
</template>

<script setup>
import { onMounted } from 'vue';
import { useTodoStore } from '@/stores/todoStore';
const store = useTodoStore()
const todos = store.todos
onMounted(() => {
  store.getTodos()
})
</script>

<style>

</style>
