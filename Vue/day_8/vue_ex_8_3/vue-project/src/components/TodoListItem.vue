<template>
  <div>
    <p>{{ todo.work }}</p>
    <p>{{ todo.content }}</p>
    <p>{{ todo.is_completed }}</p>
    <p>{{ todo.created_at }}</p>
    <RouterLink :to="{name:'TodoDetail',params:{id:todo.id}}">Detail</RouterLink>
  </div>
  <hr/>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { defineProps } from 'vue'
defineProps({
  todo: Object
})
</script>
