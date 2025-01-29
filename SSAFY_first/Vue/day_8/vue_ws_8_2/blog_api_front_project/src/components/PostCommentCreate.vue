<template>
    <div>
      <form @submit.prevent="createComment">
        <label for="comment">댓글작성: </label>
        <input type="text" id="comment" v-model.trim="commentInput">
        <input type="submit" value="작성">
      </form> <hr>
    </div>
</template>

<script setup>
import { usePostStore } from '@/stores/counter';
import { onMounted } from 'vue';
import axios from 'axios';
import { ref } from 'vue';
const commentInput = ref('')
const props = defineProps({
  post:Object
})

const store = usePostStore()
const createComment = function () {
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/${props.post.id}/comment/`,
    data: {
      content: commentInput.value,
      post: props.post.id,
    }
  })
  .then((response) => {
    console.log('댓글 작성 성공!')
    commentInput.value = ''  // 입력 필드 초기화
  })
  .catch((error) => {
    console.log(error)
  })
}
onMounted(() => {
  store.getPosts()
})
</script>

<style scoped>

</style>