import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

const el = document.getElementById('app')
if (el) {
    console.log(el.dataset)
    createApp(App).mount('#app') // id="app"
}

