import Vue from 'vue'
import Router from 'vue-router'
import user from '@/components/user'
import view from '@/components/view'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'user',
      component: user
    },
    {
      path: '/view',
      name: 'view',
      component: view
    }
  ]
})
