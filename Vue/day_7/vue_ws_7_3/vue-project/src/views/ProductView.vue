<template>
    <div>
      <h1>상품 목록 페이지</h1>
      <ProductDetail 
        v-for="product in productList"
        :key="product.id"
        :product="product"
      />
    </div>
</template>

<script setup>
import ProductDetail from '@/components/ProductDetail.vue';
import { useProductStore } from '@/stores/product';
const store = useProductStore()
const productList = store.productList
</script>

<style scoped>

</style>