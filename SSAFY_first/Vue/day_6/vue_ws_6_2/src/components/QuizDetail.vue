<template>
    <div>
      <ul>
        <li v-for="quiz in quizList" :key="quiz.pk">
          {{ quiz.question }} <br>
          <label :for="quiz.pk">정답 입력</label><br>
          <input type="text" :id="quiz.pk">
        </li>
      </ul>
    </div>
</template>

<script setup>
defineProps({
  quizList:Array
})
</script>

<style scoped>

</style>