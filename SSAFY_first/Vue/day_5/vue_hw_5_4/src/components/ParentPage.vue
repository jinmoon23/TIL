<template>
    <div>
      <ChildPage
        :children="children"
        @sendDragonMoney="sendDragonMoney"
      />
    </div>
</template>

<script setup>
import {ref} from 'vue'
import ChildPage from '@/components/ChildPage.vue';
const children = ref([
  {
    id: crypto.randomUUID(),
    name:'김하나',
    balance:100000
  },
  {
    id: crypto.randomUUID(),
    name:'김두리',
    balance:10000
  },
  {
    id: crypto.randomUUID(),
    name:'김서이',
    balance:1000
  }
])
const sendDragonMoney = function (id) {
  const childIndex = children.value.findIndex((child) => {
    return id === child.id
  })
  children.value[childIndex].balance += 1000
}
</script>

<style scoped>

</style>