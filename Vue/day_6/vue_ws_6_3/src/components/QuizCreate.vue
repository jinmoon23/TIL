<template>
    <div>
      <h3>문제를 작성해보자</h3>
      <form @submit.prevent="updateQuiz">
        <label for="question">문제</label>
        <textarea id="question" ref="questionInput"></textarea><br>
        <label for="answer">정답</label>
        <input type="text" id="answer" ref="answerInput"><br>
        <input type="submit" value="퀴즈생성">
      </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const emit = defineEmits(['updateQuiz'])
const questionInput = ref(null)
const answerInput = ref(null)
const updateQuiz = function (event) {
  const question = event.currentTarget[0].value
  const answer = event.currentTarget[1].value
  const quiz = ref({ 
    question: question,
    answer: answer
  })
  emit('updateQuiz',quiz.value)
  questionInput.value.value = ''
  answerInput.value.value = ''
}
</script>

<style scoped>

</style>