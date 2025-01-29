import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import UserProfile from '@/components/UserProfile.vue'
import UserPost from '@/components/UserPost.vue'
import LoginView from '@/views/LoginView.vue'
const isAuthenticatd = true

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  // django에서 urls.py와 유사한 구조
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    { // User 프로필로 이동하는 경로 구성, :를 통해 variable routing 기능을 구현할 수 있다.
      path: '/user/:id',
      // 첫 렌더링 시 profile을 보여주도록 하는 방법
      // name: 'user',
      component: UserView,
      // /user/:id 이후에 이어지는 주소로 작성됨
      children: [
        // 첫 렌더링 시 profile을 보여주도록 하는 방법
        {path: '',
          name: 'user',
          component: UserProfile,
         },
        {path: 'profile',
          name: 'user-profile',
          component: UserProfile,
         },
        { path: 'post',
          name: 'user-post',
          component: UserPost,
         },
      ],
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      // login 컴포넌트에 접근할 때만 아래의 코드 실행
      beforeEnter:(to,from) => {
        // console.log(to)
        // console.log(from)
        if (isAuthenticatd === true) {
          console.log('이미 로그인한 사용자 입니다.')
          return {name:'home'}  
        }
      }
    }

  ],
})
// 전역 NavigationGuard의 사용 예
// router.beforeEach((to,from) => {
//   // console.log(to)
//   // console.log(from)
//   // 로그인이 되어있지 않다면 페이지 진입을 일단 막고 login 페이지로 이동시키기
//   const isAuthenticatd = false
//   // 만약 로그인이 되어있지 않고, 이동하고자 하는 곳이 login페이지가 아니라면
//   if (!isAuthenticatd && to.name!=='login') {
//     console.log('로그인이 필요합니다')
//     return {name:'login'}
//   }
// })
export default router
