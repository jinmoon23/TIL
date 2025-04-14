import { createApp } from 'vue'
import { createPinia } from 'pinia'
// 아래 한 줄이 라이브러리 받아오면서 추가한 코드
// Persistedstate
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import App from './App.vue'

const app = createApp(App)

// 아래 2줄이 라이브러리 받아오면서 추가한 코드
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

// 이게 기본코드인데 바꿔줘야 함
// app.use(createPinia())
// 이렇게
app.use(pinia)

app.mount('#app')
