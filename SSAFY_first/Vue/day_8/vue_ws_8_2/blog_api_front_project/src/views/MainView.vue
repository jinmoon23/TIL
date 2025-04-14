<template>
    <div>
      <h1>OO의 블로그입니당</h1>
      <h3>카테고리 목록</h3>
      <CategoryView 
        v-for="category in store.categories"
        :category="category"
      />
    </div>
</template>

<script setup>
import {usePostStore} from '@/stores/counter'
import CategoryView from '@/views/CategoryView.vue';
const store = usePostStore()

</script>

<style scoped>

</style>