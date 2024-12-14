<template>
  <ul>
    <!-- 아래의 add-to-cart 를 통해 App으로 송신하기-->
    <ProductListItem 
      v-for="product in products" 
      :key="product.id" 
      :product="product"
      @add-to-cart="addToCart"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'
import Cart from '@/components/Cart.vue'

defineProps({
  products: Array
})
// 3. list는 거치기만 하고 최종 목적지인 최종 부모 App으로 송신하기
const emit = defineEmits(['addToCart'])
const addToCart = function (id) {
  emit('addToCart',id)
}
</script>
