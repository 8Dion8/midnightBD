import 'primeicons/primeicons.css';
import "primeflex/primeflex.css";
import 'primevue/resources/themes/lara-dark-purple/theme.css'
import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';

createApp(App).use(PrimeVue).mount('#app')
