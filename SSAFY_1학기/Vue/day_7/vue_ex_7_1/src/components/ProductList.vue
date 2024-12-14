<template>
    <div>
      <ul>
        <li v-for="product in productList" :key="product.id">
          {{ product.title }} - {{ product.body }}
        </li>
      </ul>
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
const store = useProductStore()
const productList = store.products
</script>

<style scoped>

</style>