<template>
    <div>
      <h1>Post 목록</h1>

      <PostListItem 
        v-for="post in store.posts"
        :post="post"
      />
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/counter';
import { onUpdated } from 'vue';
import PostListItem from '@/components/PostListItem.vue';
const store = usePostStore()
onUpdated(() => {
  store.getPosts()
})
</script>

<style scoped>

</style>