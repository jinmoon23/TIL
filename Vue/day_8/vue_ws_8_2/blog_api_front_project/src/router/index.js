import CategoryCreate from '@/components/CategoryCreate.vue'
import PostCreate from '@/components/PostCreate.vue'
import PostItemDetail from '@/components/PostItemDetail.vue'
import MainView from '@/views/MainView.vue'
import PostView from '@/views/PostView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'main',
      component: MainView
    },
    {
      path:'/category/create',
      name:'categoryCreate',
      component: CategoryCreate
    },
    {
      path:'/posts',
      name:'posts',
      component: PostView
    },
    {
      path:'/post/create',
      name:'postCreate',
      component: PostCreate
    },
    {
      path:'/post/:id',
      name:'postDetail',
      component: PostItemDetail
    },
  ],
})

export default router
