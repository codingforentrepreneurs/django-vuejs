import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

const el = document.getElementById('app')
if (el) {
    const data = {...el.dataset}
    // <App :token="abc" :user="some-user" />
    createApp(App, data).mount('#app') // id="app"
}

