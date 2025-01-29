<template>
    <div>
      <p>Post제목: {{ post.title }}</p>
      <p>Post내용: {{ post.content }}</p> 
      <button @click="toDetail(post.id)">Detail</button>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
const router = useRouter()
defineProps({
  post:Object
})
const toDetail = function (id) {
  router.push({name:'postDetail',params:{id:id}})
}
</script>

<style scoped>

</style>