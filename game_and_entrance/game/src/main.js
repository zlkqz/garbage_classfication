import Vue from 'vue'
import App from './App.vue'
//import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import DragE from './components/DragE.vue'
import tempComponent from './components/tempComponent.vue'

import VueRouter from 'vue-router'

Vue.use(VueRouter)

Vue.config.productionTip = false

const router = new VueRouter({
  routes: [
    { path: '/', name: 'DragE', component: DragE },
    { path: '/oo', name: 'tempComponent', component: tempComponent }
  ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
