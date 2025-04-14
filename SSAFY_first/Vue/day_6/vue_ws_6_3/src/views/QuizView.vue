<template>
    <div>
      <h1>Quiz</h1>
      <QuizCreate 
        @update-quiz="updateQuiz"
      />
      <ul>
        <li v-for="quiz in sortedList" :key="quiz.pk">
          {{ quiz.pk }}번 문제.
          문제: {{ quiz.question }} <br>
          정답: {{ quiz.answer }}
        </li>
      </ul>
    </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import QuizCreate from '@/components/QuizCreate.vue';
const pk = ref(0)
const quizList = ref([])
const updateQuiz = function(quiz) {
  quiz.pk = pk.value + 1
  pk.value += 1
  console.log(quiz)
  quizList.value.push(quiz)
}
const sortedList = computed(() => {
  return quizList.value.sort((a,b) => b.pk - a.pk)
})
</script>

<style scoped>

</style>