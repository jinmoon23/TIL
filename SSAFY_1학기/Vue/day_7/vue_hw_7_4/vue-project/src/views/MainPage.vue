<template>
    <div>
      <h2>메인 페이지</h2>
      <ul 
        v-for="balance in balanceList"
        :key="balance.id"
      >
      이름: {{ balance.name }} <br>
      잔고: {{ balance.balance }} <br>
      <button @click="moveToUpdate(balance.name)">updateBalance</button>
      </ul>
    </div>
</template>

<script setup>
import { useBalnaceStore } from '@/stores/counter'
const store = useBalnaceStore()
const balanceList = store.balances
const moveToUpdate = function (name) {
  store.moveToUpdate(name)
}
</script>

<style scoped>

</style>