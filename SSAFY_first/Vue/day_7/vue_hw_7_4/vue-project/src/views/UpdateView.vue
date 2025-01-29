<template>
    <div>
      <h2>데이터 수정 페이지</h2>
      이름: {{ selectedObj.name }} <br>
      잔고: {{ selectedObj.balance }} <br>
      <button @click="updateBalance(selectedObj.name)">+</button>
      <!-- <button @click="getterWithArgs(selectedObj.name)">+</button> -->
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useBalnaceStore } from '@/stores/counter';
const store = useBalnaceStore()
const route = useRoute()
const balanceList = store.balances
// params에서 name 추출
const selectedName = route.params.name
// name과 일치하는 객체를 찾아 그 객체의 인덱스 반환
const index = balanceList.findIndex((balance) => {
  return selectedName === balance.name
})
// 내가 선택한 그 오브젝트에 접근
const selectedObj = balanceList[index]

const updateBalance = function (name) {
  store.updateBalance(name)
}


</script>

<style scoped>

</style>