<template>
  <li v-for="product in products" :key="product.id">
    <ProductListItem :prop-product="product"/>
    <!-- {{ product.name }} - {{ product.price }}원 -->
  </li>
  
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue';
defineProps({
  products: Array
})
</script>
