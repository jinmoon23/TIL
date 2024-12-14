<template>
    <div>
      <TodoListItem
        :todo="todo"
      />
    </div>
</template>

<script setup>
defineProps({
  todo:Object
})
import TodoListItem from '@/components/TodoListItem.vue';
</script>

<style scoped>

</style>