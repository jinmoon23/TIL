import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const products = ref([
    {id:crypto.randomUUID(),title:'베럴 서핑 모자',body:'아주 찰떡입니다'},
    {id:crypto.randomUUID(),title:'베럴 서핑 수트',body:'아주 콩떡입니다'},
    {id:crypto.randomUUID(),title:'베럴 서핑 신발',body:'아주 찹쌀입니다'}
  ])
  return {
    products
  }
})
