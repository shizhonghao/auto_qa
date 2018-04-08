/**
 * Created by 施中昊 on 2018/4/6.
 */
import Vue from 'vue'
import Router from 'vue-router'
import answer from '@/admin_components/answer'
import login from '@/admin_components/login'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/answer',
      name: 'answer',
      component: answer
    },
    {
      path: '/login',
      name: 'login',
      component: login
    }
  ]
})
