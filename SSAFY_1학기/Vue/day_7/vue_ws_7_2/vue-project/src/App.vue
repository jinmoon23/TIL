<template>
  <div>
    <nav>
      <RouterLink :to="{name:'home'}">Home</RouterLink> | 
      <RouterLink :to="{name:'products'}">상품 목록</RouterLink> | 
      <RouterLink :to="{name:'favorite'}">장바구니</RouterLink>
    </nav>
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>