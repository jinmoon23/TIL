<template>
  <div>
    <header>명함 관리 페이지</header>
    <main>명함을 관리하는 페이지 입니다. 여기에 명함 목록이 표시됩니다.</main>
    <article>
      <BusinessCard/>
    </article>
    <footer>@2023 My business Cards</footer>
  </div>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue';
</script>

<style scoped>

</style>