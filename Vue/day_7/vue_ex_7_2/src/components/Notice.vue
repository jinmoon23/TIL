<template>
    <div>
      재고상품: {{ stockProduct }}
    </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
import { computed } from 'vue';
const store = useProductStore()
// computed로 정의된 값은 computed로 받아서 써야
// 반응형으로 정상 동작함!
const stockProduct = computed(() => {
  return store.stockProduct
})
</script>

<style scoped>

</style>