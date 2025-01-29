<template>
    <div>
      {{ myMsg }}
      <button @click="updateName">직전 부모에 이름 변경 요청하기</button>
    </div>
</template>

<script setup>
defineProps({
    myMsg:String
})
const emit = defineEmits(['updateName'])
const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>