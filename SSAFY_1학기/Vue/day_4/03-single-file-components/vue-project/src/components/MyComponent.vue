<template>
    <div>
      <h2>MyComponent</h2>
      <!-- 컴포넌트는 재사용 가능한 코드블럭이다! -->
      <!-- 따라서 반복해서 사용해도 됨 ㅎㅎ -->
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>
      <MyComponentItem/>
      <!-- 당연히 v-for도 가능함 -->
      <!-- <MyComponentItem v-for/> 등등이 가능 -->
    </div>
    <!-- 이런식으로 가능하지만 컴포넌트의 최상위 태그는 하나만 하는것이 좋다. -->
    <div>
      <a href="">ssafy</a>
    </div>
</template>

<script setup>
import MyComponentItem from '@/components/MyComponentItem.vue';
</script>

<!-- 1. lang="scss" 삭제하기 -->
<style lang="scss" scoped>

</style>