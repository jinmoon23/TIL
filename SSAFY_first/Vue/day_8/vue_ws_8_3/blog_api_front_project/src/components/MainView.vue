<template>
    <div>
      <h1>OO의 블로그입니당</h1>
      <ul v-for="post in store.posts">
        {{ post.title }}
        {{ post.content }}
      </ul>
    </div>
</template>

<script setup>
import {usePostStore} from '@/stores/counter'
import { onMounted } from 'vue';
const store = usePostStore()
onMounted(() => {
  store.getPosts()
})

</script>

<style scoped>

</style>