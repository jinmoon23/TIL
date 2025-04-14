<template>
<main>
  <h1>할 일 목록</h1>
  <TodoList 
    v-for="todo in todos"
    :key="todo.id"
    :todo="todo"
  />
</main>
</template>

<script setup>
import { onMounted } from 'vue'
import {useTodoStore} from "@/stores/todoStore.js";
import TodoList from '@/components/TodoList.vue';
const store = useTodoStore()
const todos = store.todos
onMounted(() => {
  store.getTodos()
})

</script>

<style>

</style>
