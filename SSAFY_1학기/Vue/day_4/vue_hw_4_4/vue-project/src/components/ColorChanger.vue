<template>
    <div>
      <input type="text" v-model="input">
      <p :class="input">입력창에 올바른 색상 명을 입력하면 이 문장의 글자색이 바뀝니다 ㅎㅎ 신기하죠 촤하하하하하</p>
    </div>
</template>

<script setup>
import {ref} from 'vue'

const input = ref('')

</script>

<style scoped>
.red {
  color: red;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
</style>