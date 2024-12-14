<template>
  <div>
    <h1>퀴즈앱</h1>
    <h3>지금 바로 도전해보세요!</h3>
    <RouterLink :to="{name:'home'}">Home</RouterLink> | 
  </div>
  <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<style scoped>

</style>