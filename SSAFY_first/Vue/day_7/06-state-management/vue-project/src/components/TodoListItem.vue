<template>
    <div>
      <!-- 해당 span 태그를 클릭하면 updateTodo 액션이 동작하도록 구현 -->      
      <span 
        @click="store.updateTodo(todo.id)"
        :class="{'is-done':todo.isDone}"
      >
        {{ todo.text }}
      </span>
      <!-- 이번에는 직접 호출로 삭제기능 구현 -->
      <button @click="store.deleteTodo(todo.id)">todo삭제</button>
    </div>
</template>

<script setup>
defineProps({
  todo:Object
})
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()
</script>

<style scoped>
.is-done {
  text-decoration: line-through;
}
</style>