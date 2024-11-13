<template>
    <div>
      <ul>
        {{ todo.work }} <br>
        {{ todo.content }} <br>
        {{ todo.is_completed }} <br>
        {{ todo.created_at }} <br>
        <RouterLink :to="{name:'todoDetail',params:{id:todo.id}}">Detail</RouterLink>
      </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import TodoDetail from './TodoDetail.vue';
defineProps({
  todo:Object
})
</script>

<style scoped>

</style>