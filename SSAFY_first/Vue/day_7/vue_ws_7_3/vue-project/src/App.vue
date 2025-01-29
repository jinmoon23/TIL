<template>
  <div>
    <nav>
      <RouterLink :to="{name:'home'}">Home</RouterLink> | 
      <RouterLink :to="{name:'products'}">상품 목록</RouterLink> | 
      <RouterLink :to="{name:'favorite'}">장바구니 {{ cartCount }}</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { RouterLink, RouterView } from 'vue-router';
import { useProductStore } from './stores/product';
const store = useProductStore()
const cartCount = computed (() => {
  return store.cartCount
})

</script>

<style scoped>

</style>