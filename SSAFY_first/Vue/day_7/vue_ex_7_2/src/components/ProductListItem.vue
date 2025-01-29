<template>
    <div>
      <li>
        {{ product.title }} - {{ product.body }}
        <button @click="deleteProduct(product.id)">상품삭제</button>
      </li>
    </div>
</template>

<script setup>
defineProps({
  product:Object
})
import { useProductStore } from '@/stores/product'
const store = useProductStore()
const deleteProduct = function (productId) {
  store.deleteProduct(productId)
}
</script>

<style scoped>

</style>