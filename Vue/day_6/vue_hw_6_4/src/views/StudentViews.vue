<template>
    <div>
      <ul>
        <li v-for="student in students">
          {{ student.name }} 학생 정보 보기
        </li>
      </ul>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const students = ref([
  {name:'김하나'},
  {name:'김두리'},
  {name:'김서이'},
])
</script>

<style scoped>

</style>