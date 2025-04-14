<template>
    <div>
      <h1>Parent 페이지 입니다.</h1>
      <ChildPage
        :children="children"
      />
    </div>
</template>

<script setup>
import {ref} from 'vue'
import ChildPage from '@/components/ChildPage.vue';
  const children = ref([
    { id: crypto.randomUUID(),
      name: '김하나',
      age: 30
    },
    {id: crypto.randomUUID(),
      name: '김두리',
      age: 20
    },
    {id: crypto.randomUUID(),
      name: '김서이',
      age: 10
    }
  ])
</script>

<style scoped>

</style>