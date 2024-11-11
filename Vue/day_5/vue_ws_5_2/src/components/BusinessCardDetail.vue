<template>
    <div>
      <ul>
        <li v-for="card in businessCards">
          <p>이름: {{ card.name }}</p>
          <p>직함: {{ card.title }}</p>
        </li>
      </ul>
    </div>
</template>

<script setup>

defineProps({
    businessCards: Array 
})
</script>

<style scoped>

</style>