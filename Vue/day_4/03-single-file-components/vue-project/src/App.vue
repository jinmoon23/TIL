<template>
<h1>App.vue</h1>
<!-- 3. 호출 -->
<MyComponent />
</template>

<script setup>
// 2. App.vue import
// import MyComponent from './components/MyComponent.vue'
// ./components는 반복된다.
// src가 핵심이므로 src를 위한 절대경로를 정의했음
// 여기서 @/ == src, 자주 사용하는 약어라고 생각하면 됨
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>

</style>
