import Vue from 'vue'
import Router from 'vue-router'

import main from '../views/main.vue'
import Login from '../components/Login.vue'
import SignUp from '../components/SignUp'
    
Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes:[
    {
      path: '/main',
      name: 'main',
      component: main
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/SignUp',
      name: 'signup',
      component: SignUp
    }
  ]
})

