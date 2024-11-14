<template>
    <div>
      <h1>카테고리 생성 페이지</h1>
      <form @submit.prevent="createCategory">
        <label for="name">카테고리 이름</label>
        <input type="text" id="name" v-model.trim="nameInput"> <br>
        <input type="submit" value="생성하기">
      </form>
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/counter';
import { ref } from 'vue';
const nameInput = ref('')
const store = usePostStore()
const createCategory = function () {
  const payLoad = {
    name: nameInput.value
  } 
  store.createCategory(payLoad)
}

</script>

<style scoped>

</style>