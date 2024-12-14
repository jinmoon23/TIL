<template>
  <div class="quiz-app">
    <div class="app-header">
      <!-- 앱 이름 -->
      <h1>Quiz 앱 입니다</h1>
    </div>
    <div class="app-description">
      <!-- 앱 설명 -->
      <h3>같이 문제를 풀어보아요</h3>
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
