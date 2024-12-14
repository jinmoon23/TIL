<template>
  <div>
    <MainPage/>
    <RouterLink :to="{name:'some'}">SOME</RouterLink> | 
    <RouterLink :to="{name:'other'}">OTHER</RouterLink>
  </div>
  <RouterView/>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>