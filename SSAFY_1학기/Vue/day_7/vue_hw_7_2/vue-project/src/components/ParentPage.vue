<template>
    <div>
      <h2>부모 컴포넌트</h2>
      <p>아버지: {{ family.father }}</p>
      <p>어머니: {{ family.mother }}</p>
      <ChildPage 
        v-for="child in family.children"
        :key="child.id"
        :child="child"
      />
    </div>
</template>

<script setup>
import ChildPage from '@/components/ChildPage.vue';
defineProps({
  family:Object
})
</script>

<style scoped>

</style>