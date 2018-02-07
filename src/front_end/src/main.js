// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import VueResource from 'vue-resource'
import axios from 'axios'

Vue.use(VueResource)
Vue.use(ElementUI)

Vue.prototype.$ajax = axios
axios.defaults.withCredentials = true
axios.defaults.baseURL = 'localhost:5000'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App),
  //store
  //components: { App },
  //template: '<App/>'
})
