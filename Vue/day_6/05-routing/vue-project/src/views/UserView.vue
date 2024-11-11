<template>
    <div>
      <h1>UserView</h1>
      <!-- 내부변수객체($route)의 params 객체에 routing 데이터에 접근 가능-->
      <h2>{{$route.params.id}}번 유저의 프로필 페이지입니다.</h2>
      <h2>{{userId}}번 유저의 프로필 페이지입니다.</h2>
      <button @click="goHome">홈으로!</button>
      <button @click="routeUpdate">100 유저 페이지로!</button>
      <RouterLink :to="{name:'user-profile'}">Profile</RouterLink>
      <RouterLink :to="{name:'user-post'}">Post</RouterLink>
      <hr>
      <RouterView />
    </div>
</template>

<script setup>
// 위의 방식으로 하면 코드가 복잡해지는 문제가 있음
// 그래서 스크립트에서 처리 후 간단하게 전달하는 방식이 있음
// useRouter 는 프로그래밍적으로 패스를 구성하기 위한 메서드
import { useRoute, useRouter, RouterLink, RouterView, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'
import {ref} from 'vue'

// 컴포넌트에서 떠날 때 특정한 동작을 수행하기
onBeforeRouteLeave((to,from) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

// 해당 방법으로 접근하면 userId를 스크립트에서 활용할 수 있음
const route = useRoute()
const userId = ref(route.params.id)
// 프로그래밍적으로 패스를 구성하기
const router = useRouter()
const goHome = function () {
  // push는 나의 흔적을 남겨서 뒤로가기가 가능함
  // router.push({name:'home'})
  // replace는 나의 흔적을 남기지 않기 때문에 뒤로가기가 불가능함
  router.replace({name:'home'})
}
const routeUpdate = function () {
  router.push({name:'user', params:{id:100}})
}
onBeforeRouteUpdate((to,from) => {
  userId.value = to.params.id
})
</script>

<style  scoped>

</style>