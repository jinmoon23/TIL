<template>
    <div>
      <p>{{ myMsg }}</p>
      <p>{{ dynamicProps }}</p>
      <!-- {{ myMessage }} -->
      <!-- 여기서 v-vind 하지 않으면 그냥 문자열을 전달하는 꼴이 됨! -->
      <ParentGrandChild 
        :my-msg="myMsg"
        @updateName="updateName"
      />
      <!-- 커스텀 이벤트 이름을 인자로 전달 -->
      <!-- <button @click="$emit('someEvent')"></button> -->
      <!-- 이런 방식으로 emit을 구성할 수 있고 더 권장되는 방식임 -->
      <button @click="btnClick">클릭비</button>
      <button @click="emitArgs">인자 전달하기</button>
    </div>
</template>

<script setup>
// 내려받은 props를 선언한 후 데이터 사용
// 인자는 객체 또는 배열을 받는다.
// 부모측에서 내려보낼 때 표기 방식이 서로 다르다.
// 부모측은 케밥케이스 / 자식측은 카멜케이스 -> 영역을 떠올리면 다 해결된다.
// 부모측에서 props 사용시 HTML / 자식측에서 선언 후 사용할 때는 JS

// 1. 문자열 배열 선언방식
// defineProps(['myMsg'])
// defineProps(['myMessage'])

// 2. 객체 선언 방식
defineProps({
  myMsg: String,
  // 3. 동적 props
  dynamicProps:String,
})
// props 데이터를 JS에서 활용하려면
// const props = defineProps({myMsg:String})
// console.log(props)  
// console.log(props.myMsg)

import ParentGrandChild from '@/components/ParentGrandChild.vue';

// emit 이벤트 선언 후 사용하기
// 배열 방식과 객체 방식 모두 가능
// 첫 번째 인자는 커스텀 이벤트, 두번째 인자는 부모에 전달할 데이터
const emit = defineEmits(['someEvent', 'emitArgs', 'updateName'])

const btnClick = function () {
  emit('someEvent')
}
const emitArgs = function () {
  emit('emitArgs', 1, 2, 3)
}

const updateName = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>