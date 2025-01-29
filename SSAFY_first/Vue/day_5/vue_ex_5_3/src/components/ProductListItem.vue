<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="addToCart(product.id)">장바구니에 추가</button>
  </li>
</template>

<script setup>
defineProps({
  product: Object
})
// 1. emit을 통해 장바구니 버튼을 눌렀을 때 cart에 추가하도록 하기
// 먼저 emit 변수 배열에 addToCart 함수 추가
const emit = defineEmits(['addToCart'])
const addToCart = function (id) {
  // 2. addToCart 버튼을 누르면 emit 동작하면서 부모(ProductList)로 product.id송신
  emit('addToCart',id)
}

</script>

<style scoped>

</style>