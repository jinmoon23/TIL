<template>
    <div>
      <br>
      <form @submit.prevent="createPost">
        <label for="category">카테고리 선택</label>
        <select id="category" v-model="categoryInput">
          <option v-for="category in store.categories">
            {{ category.name }}
          </option>
        </select> <br>
        <label for="title">제목</label>
        <input type="text" id="title" v-model.trim="titleInput"><br>
        <label for="content">내용</label>
        <textarea id="content" v-model.trim="contentInput"></textarea><br>
        <input type="submit" value="생성하기">
      </form>
    </div>
</template>

<script setup>
import axios from 'axios';
import { usePostStore } from '@/stores/counter';
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { onMounted } from 'vue';

const router = useRouter()
const titleInput = ref('')
const contentInput = ref('')
const categoryInput = ref('')
const store = usePostStore()
const createPost = function () {
  axios({
    method:'post',
    url:`${store.API_URL}/api/v1/posts/`,
    data:{
      title: titleInput.value,
      content: contentInput.value,
      category: categoryInput.value
    }
  })
  .then((response) => {
    console.log('POST 저장 완료')
    router.push({name:'posts'})
  })
  .catch((error) => {
    console.log(error)
  })
}
onMounted(() => {
  store.getCategories()
})
</script>

<style scoped>

</style>