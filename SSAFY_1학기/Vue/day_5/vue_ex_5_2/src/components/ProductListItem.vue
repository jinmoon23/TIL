<template>
    <div>
      {{ propProduct.name }} - {{ propProduct.price }}
      <button>장바구니 추가</button>
    </div>
</template>

<script setup>
defineProps({
  propProduct:Object
})
</script>

<style scoped>

</style>