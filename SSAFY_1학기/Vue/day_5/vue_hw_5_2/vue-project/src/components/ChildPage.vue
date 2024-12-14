<template>
    <div v-for="child in children" :key="child.id">
      <h3>Child 페이지 입니다.</h3>
      <p>이름: {{ child.name }}</p>
      <p>나이: {{ child.age }}</p>
    </div>
</template>

<script setup>
defineProps({
  children: Array
})
</script>

<style scoped>

</style>