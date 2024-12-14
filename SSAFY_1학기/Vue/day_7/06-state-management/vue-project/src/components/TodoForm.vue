<template>
    <div>
      TodoForm
      <form @submit.prevent="createTodo(todoText)" ref="formElement">
        <input type="text" v-model="todoText">
        <input type="submit" value="addTodo">
      </form>
    </div>
</template>

<script setup>
import {ref} from 'vue'
const todoText = ref('')
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()
// ref를 활용해 DOM 직접 선택하기
const formElement = ref(null)
// 간접적으로 호출하기 -> 장기적인 관점에서 볼 때 추가적인 코드를
// 작성하는 경우 더 유리함
const createTodo = function (todoText) {
  store.addTodo(todoText)
  // 여기 추가적인 코드가 작성될 수 있다.
  // 예를들어 addTodo() 메서드가 동작한 이후 input 태그를 지우기
  formElement.value.reset()
  // 이처럼 초기엔 조금 더 번잡하지만 이후 추가적인 동작을 설정할 수 있어서 유지보수가 편리해짐 
}
 
</script>

<style scoped>

</style>