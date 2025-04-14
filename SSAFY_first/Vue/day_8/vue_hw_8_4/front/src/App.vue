<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{name:'home'}">Home</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
