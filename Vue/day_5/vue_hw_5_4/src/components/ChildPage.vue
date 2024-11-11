<template>
    <div v-for="child in children" :key="child.id">
      <h3>자식 페이지입니다.</h3>
      <p>이름: {{ child.name }}</p>
      <p>용돈: {{ child.balance }}</p>
      <button @click="sendDragonMoney(child.id)">아빠 용돈 주세요~!!</button>
    </div>
</template>

<script setup>
defineProps({
  children:Array
})

const emit = defineEmits(['sendDragonMoney'])
const sendDragonMoney = function (id) {
  emit('sendDragonMoney',id)
}
</script>

<style scoped>

</style>