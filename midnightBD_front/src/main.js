import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import Aura from './themes/aura';


const app = createApp(App)
app.use(PrimeVue, { unstyled: true, pt: Aura })
app.mount('#app')
