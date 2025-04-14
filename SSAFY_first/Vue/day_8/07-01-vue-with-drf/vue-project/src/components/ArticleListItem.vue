<template>
  <div>
    <ul>
      게시글 id: {{ article.id }} <br>
      {{ article.title }} - {{ article.content }}
      <RouterLink :to="{name:'DetailView', params:{id:article.id}}">DetailPage</RouterLink>
    </ul>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
defineProps({
  article:Object
})
</script>
