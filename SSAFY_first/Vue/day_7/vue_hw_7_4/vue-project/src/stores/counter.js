import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


export const useBalnaceStore = defineStore('balance', () => {
  const balances = ref([
    { id:crypto.randomUUID(),
      name: '김하나',
      balance: 100000
      },
      {id:crypto.randomUUID(),
      name: '김두리',
      balance: 10000
      },
      {id:crypto.randomUUID(),
      name: '김서이',
      balance: 100
      },
  ])
  const router = useRouter()
  const moveToUpdate = function (name) {
    // route의 params로 접근해 'update'에서 
    // name을 추출해서 사용할 수 있음
    router.push({name:'update', params:{name:name}})
  }

  const updateBalance = function (name) {
    const index = balances.value.findIndex((balance) => {
      return balance.name === name
    })
    balances.value[index].balance += 1000
  }
  return {
    balances,
    moveToUpdate,
    updateBalance,
    // getterWithArgs,
  }
})
