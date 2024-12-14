<template>
  <div>
    <RouterLink :to="{name:'main'}">main</RouterLink> | 
    <RouterLink :to="{name:'posts'}">post</RouterLink> | 
    <RouterLink :to="{name:'postCreate'}">postCreate</RouterLink> | 
    <RouterLink :to="{name:'categoryCreate'}">categortCreate</RouterLink>
  </div>
  <RouterView/>
</template>

<script setup>
import { usePostStore } from './stores/counter';
import { RouterLink, RouterView } from 'vue-router';
import { onMounted, onUpdated } from 'vue';
const store = usePostStore()
onMounted(() => {
  store.getPosts()
  store.getCategories()
})
onUpdated(() => {
  store.getPosts()
})
</script>

<style scoped>

</style>