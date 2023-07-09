import { createApp } from 'vue'
import App from './App.vue'
import VueDatePicker from '@vuepic/vue-datepicker';
import Toast from "vue-toastification";
import "@/assets/reset.css"
import '@vuepic/vue-datepicker/dist/main.css';
import 'bootstrap-icons/font/bootstrap-icons.css'
import "bootstrap/dist/css/bootstrap.min.css"
import "vue-toastification/dist/index.css";
import "@/assets/style.css"
import "bootstrap"


const app = createApp(App);

app.component('VueDatePicker', VueDatePicker);
app.use(Toast, {});
app.mount('#app')
