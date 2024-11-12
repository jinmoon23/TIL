<template>
    <div>
      <h1>pinia 연습하기</h1>
      <ParentPage 
        v-for="family in familyInfo"
        :key="family.id"
        :family="family"
      />
    </div>
</template>

<script setup>
import ParentPage from '@/components/ParentPage.vue'
import { useFamilyStore } from '@/stores/family'
const store = useFamilyStore()
const familyInfo = store.familyInfo
</script>

<style scoped>

</style>