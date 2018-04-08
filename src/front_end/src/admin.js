/**
 * Created by 施中昊 on 2018/4/6.
 */
import Vue from 'vue'
import admin from './admin.vue'
import router from './admin_router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
//import VueResource from 'vue-resource'
import axios from 'axios'
import VueAxios from 'vue-axios'


//Vue.use(VueResource)
Vue.use(ElementUI)
Vue.use(VueAxios,axios)

//Vue.prototype.$ajax = axios
//axios.defaults.withCredentials = true
//axios.defaults.baseURL = 'localhost:5000'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#admin',
  router,
  render: h => h(admin)
})
