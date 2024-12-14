<script setup>
import { RouterLink, RouterView } from 'vue-router'
import {ref} from 'vue'
const studentName = ref('김하나')
</script>

<template>
  <header>
    <div class="wrapper">
      <MainPage />
      <nav>
        <!-- <RouterLink to="/"></RouterLink> -->
         <RouterLink :to="{name:'students'}">students</RouterLink>
         <RouterLink :to="{name:'students', params:{name:studentName}}">studentDetail</RouterLink>
      </nav>
    </div>
    <RouterView/>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
