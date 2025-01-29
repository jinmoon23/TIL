<template>
    <div>
      <TodoListItem 
        v-for="todo in store.todos"
        :key="todo.id"
        :todo="todo"
      />
    </div>
</template>

<script setup>
import TodoListItem from '@/components/TodoListItem.vue'
// props를 통해 데이터를 전달하기 위해 store의 데이터를 받아옴
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
console.log(store.todos)
</script>

<style scoped>

</style>