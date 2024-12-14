<template>
    <div>
      <img :src="product.imagePath" alt="" width="200">
      <p>상품명: {{ product.name }}</p>
      <p>가격: \ {{ product.price }}</p>
      <button @click="cart(product.id)">장바구니 담기 {{ product.isFavorite }}</button>
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product';
const store = useProductStore()
const cart = function (id) {
  store.cart(id)
}
defineProps({
  product:Object
})

</script>

<style scoped>

</style>