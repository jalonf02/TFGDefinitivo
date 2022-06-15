import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import PandeoLateral from '@/components/PandeoLateral'
import PandeoCompresion from '@/components/PandeoCompresion'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path: '/PandeoLateral',
      name: 'PandeoLateral',
      component: PandeoLateral
    },
    {
      path: '/PandeoCompresion',
      name: 'PandeoCompresion',
      component: PandeoCompresion
    }
  ],
  mode: 'history'
})
