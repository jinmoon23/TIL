<template>
    <div>
      <!-- 여기서 props 설정 -->
      <!-- parent가 child에게 message 데이터를 전달한 것 -->
      <ParentChild 
        my-msg="이것이 Props?!"
        :dynamic-props="name"
        @some-event="someCallback"
        @emit-args="getNumbers"
        @updateName="updateName"
      />
      <ParentItem 
        v-for="item in items" 
        :key="item.id"
        :my-props="item"
      />
    </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue';
import ParentItem from '@/components/ParentItem.vue';
import {ref} from 'vue'

const name = ref('Alice')

// 반복연습

const items = ref([
  {id:1, name: '사과'},
  {id:2, name: '바나나'},
  {id:3, name: '딸기'},
])
const someCallback = function () {
  console.log('자식 컴포넌트에서 발신한 이벤트를 정상적으로 수신했어요~!! ')
}
const getNumbers = function (...args) {
  console.log('자식 컴포넌트에게서 받은 데이터 입니다~')
  console.log(args)
}

const updateName = function() {
  console.log('되고 있니??')
  name.value = 'Bella'
}

</script>

<style scoped>

</style>