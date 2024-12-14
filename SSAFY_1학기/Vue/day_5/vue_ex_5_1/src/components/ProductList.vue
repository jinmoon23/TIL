<template>
    <div>
      <li v-for="product in propProducts" :key="product.id">
        {{ product.name }} - {{ product.price }}
      </li>
    </div>
</template>

<script setup>
// 2. 자식 컴포넌트에서 props 수신
defineProps({
    propProducts: Array
})
</script>

<style scoped>

</style>