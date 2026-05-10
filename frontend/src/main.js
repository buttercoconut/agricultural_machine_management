import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

// Set base URL for axios
axios.defaults.baseURL = process.env.VUE_APP_API_BASE_URL || 'http://localhost:8000/api';

const app = createApp(App);
app.use(router);
app.use(store);
app.config.globalProperties.$axios = axios;
app.mount('#app');
