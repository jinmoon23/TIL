<template>
    <div>
      카테고리 이름: {{ category.name }}
    </div>
</template>

<script setup>
defineProps({
  category:Object
})
</script>

<style scoped>

</style>