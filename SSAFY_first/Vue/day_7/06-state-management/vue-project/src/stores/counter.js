// import { ref, computed } from 'vue'
// import { defineStore } from 'pinia'
// // 'counter'는 store의 고유 ID
// export const useCounterStore = defineStore('counter', () => {
//   // 1. state === data 정의
//   const count = ref(0)
//   // 2. getters === computed 계산된 값 정의
//   const doubleCount = computed(() => count.value * 2)
//   // 3. action === function 메서드 정의
//   function increment() {
//     count.value++
//   }
//   // 4. pinia의 상태들을 사용하려면 반드시 반환해야 함.
//   // 객체를 리턴함
//   return { count, doubleCount, increment }
// })

// // store 디렉터리 상 js파일의 주의점!
// // 공유하지 않을 예정인 상태 속성을 저장하지 않는다.
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  // 1. state 정의
  let id = 0
  const todos = ref([
  ])
  // 2. addTodo action 정의
  const addTodo = function (todoText) {
    todos.value.push(
      {
        id: id++,
        text:todoText,
        isDone:false
      }
    )
  }
  // 3. deleteTodo action 정의
  const deleteTodo = function (selectedId) {
    const selectedIndex = todos.value.findIndex((todo) => {
      return selectedId === todo.id
    })
    todos.value.splice(selectedIndex,1)
  }
  // 4. updateTodo action 정의
  const updateTodo = function (selectedId) {
    // 수정된 값만 변경하고 나머지는 그대로 배열에 넣기
    todos.value = todos.value.map((todo) => {
      if (selectedId === todo.id) {
        todo.isDone = !todo.isDone
      }
      return todo
    })
  }
  // 5. 완료한 todo의 갯수를 구하기 위해 getters 정의
  const doneTodoCount = computed(() => {
    const doneTodos = todos.value.filter((todo) => {
      return todo.isDone
    })
    return doneTodos.length
  })
  return {
    todos,
    addTodo,
    deleteTodo,
    updateTodo,
    doneTodoCount,
  }
},
// 아래 코드를 추가하여 Persistedstate 라이브러리 설정을 끝냄
{
  persist:true
})