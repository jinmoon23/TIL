import { createRouter, createWebHistory } from 'vue-router'
import TodoView from '@/views/TodoView.vue'
import TodoDetail from '@/components/TodoDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'TodoView',
      component: TodoView
    },{
      path: '/:id',
      name: 'todoDetail',
      component: TodoDetail
    },
  ]
})

export default router
