<template>
    <div>
      <h1>Quiz</h1>
      <QuizDetail :quiz-list="quizList"/>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import QuizDetail from '@/components/QuizDetail.vue'
const quizList = ref([
  {
    pk:crypto.randomUUID(),
    question:'푸하핫1',
    answer:'flask'
  },
  {
    pk:crypto.randomUUID(),
    question:'푸하핫1',
    answer:'flask'
  },
  {
    pk:crypto.randomUUID(),
    question:'푸하핫2',
    answer:'input'
  },
  {
    pk:crypto.randomUUID(),
    question:'푸하핫3',
    answer:'post'
  },
  {
    pk:crypto.randomUUID(),
    question:'푸하핫4',
    answer:'virtualenv'
  },
  {
    pk:crypto.randomUUID(),
    question:'푸하핫5',
    answer:'html'
  }
])
</script>

<style scoped>

</style>