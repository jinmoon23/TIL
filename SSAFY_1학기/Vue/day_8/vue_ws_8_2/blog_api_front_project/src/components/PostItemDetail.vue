<template>
    <div>
      <h1>게시글 상세 조회</h1>
      <p>카테고리명: {{ post.category }}</p>
      <p>{{ post.id }}번째 글</p>
      <h3>Post제목: {{ post.title }}</h3><hr>
      <p>작성일: {{ post.created_at }}</p>
      <p>수정일: {{ post.updated_at }}</p><hr>
      <p>Post내용: {{ post.content }}</p><hr>
      <PostCommentCreate
        :post="post"
      />
      <PostCommentList 
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"  
      />
    </div>
</template>

<script setup>
import { useRoute, useRouter } from 'vue-router';
import PostCommentList from '@/components/PostCommentList.vue';
import PostCommentCreate from '@/components/PostCommentCreate.vue';
import { usePostStore } from '@/stores/counter';
import { onMounted, ref, onUpdated } from 'vue';
import axios from 'axios';

const store = usePostStore()
const router = useRouter()
const comments = ref([])
const route = useRoute()
const postId = route.params.id
console.log(postId)
console.log(store.posts)
const index = store.posts.findIndex((post) => {
  console.log(post)
  // post.id는 Int고 postId는 String
  // 따라서 ===가 아닌 ==로 확인해야함!
  return post.id == postId
})
const post = store.posts[index]
onMounted(() => {
  getComments()
})
const getComments = function () {
  axios({
    method:'get',
    url:`${store.API_URL}/api/v1/${postId}/comment/`
  })
  .then((response) => {
    comments.value = response.data.comments
  })
  .catch((error) => {
    console.log(error)
  })
}
onUpdated(() => {
  getComments()
  store.getPosts()
})

</script>

<style scoped>

</style>