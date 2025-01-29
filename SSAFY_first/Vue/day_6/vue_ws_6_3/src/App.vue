<template>
  <div class="quiz-app">
    <div class="app-header">
      <!-- 앱 이름 -->
       <h1>퀴즈 풀자~</h1>
    </div>
    <div class="app-description">
      <!-- 앱 설명 -->
       <h3>이자슥아~</h3>
    </div>
    <nav class="app-nav">
      <RouterLink :to="{name:'home'}" class="nav-link">Home</RouterLink> |
      <RouterLink :to="{name:'quiz'}" class="nav-link">Quiz</RouterLink> 
    </nav>
  </div>
  
  <RouterView />
</template>

<script setuo>
import { RouterLink, RouterView } from 'vue-router';
</script>

<style scoped>

</style>
