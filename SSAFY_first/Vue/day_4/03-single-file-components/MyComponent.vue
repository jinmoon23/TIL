<!-- 태그들의 순서는 상관없으나 일반적으로 따르는 규칙은 있음! -->
<!-- 일반적인 규칙: template -> script -> style -->

<template>
    <div class="greeting">
      {{ msg }}
    </div>
</template>

<!-- vue CDN 필요없음! -->
<!-- script 태그 자체가 setup 함수임! -->
<!-- script 태그는 몇 개를 사용해도 무관하지만 script setup 태그는 하나만 가능! -->
<script setup>
// Vue가 아닌 vue임!
import {ref} from 'vue'
const msg = ref('hello')
// 이제 return 없이도 정상동작함.
</script>

<!-- scoped에 의해 이 컴포넌트에서만 실행됨! -->
<style  scoped>
.greeting {
  color: red;
}

</style>