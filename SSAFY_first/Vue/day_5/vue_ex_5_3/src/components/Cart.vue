<template>
    <div>
      <h2>장바구니</h2>
      <ul>
        <li v-for="cartProduct in cartProducts" :key="cartProduct.id">
          {{ cartProduct.name }} - {{ cartProduct.price }}
          <button @click="deleteCartItem(cartProduct)">삭제</button>
        </li>
      </ul>
    </div>
</template>

<script setup>
// 5. App 부모로부터 받은 Cart 배열을 받아 표현하기
defineProps({
    cartProducts: Array
})
const emit = defineEmits(['deleteCartItem'])
const deleteCartItem = function (cart) {
  emit('deleteCartItem', cart)
}

</script>

<style scoped>

</style>