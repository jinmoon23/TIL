# day_6 Routing

CSR에서 Routing은 클라이언트가 담당.
  - 네트워크에서 경로를 선택하는 프로세스
  - 웹 어플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

이제는 `npm create vue@latest` 후 router 관련 부분에서 yes 선택함!

## 변동사항
App.vue
main.js
router 폴더 생성
  - 내부의 index.js 파일에 routes 배열이 있음
  - 이 배열에 path 작성하여 routing 함!

## 매개변수를 사용한 동적 경로 매칭(django variable routing과 동일)

  1. UserView.vue 생성
  2. index.js path 추가

## Route와 Router
매개변수를 활용한 동적 경로 매칭 시 사용하는 route.
프로그래머틱 네비게이션 경로 이동 시 사용하는 router.

route의 활용
```javascript
import {ref} from 'vue'
import {useRoute} from 'vue-router'
const route = useRoute()
const userId = ref(route.params.id)
```
router의 활용
```javascript
import {useRouter} from 'vue-router'
const router = useRouter()
const goHome = function () {
  router.push({name:'home'})
}
```