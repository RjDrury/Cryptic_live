import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _ba05daac = () => interopDefault(import('../pages/topstreams.vue' /* webpackChunkName: "pages/topstreams" */))
const _2d58a088 = () => interopDefault(import('../pages/game/_twitch/_mixer.vue' /* webpackChunkName: "pages/game/_twitch/_mixer" */))
const _4aa2dcd6 = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/topstreams",
    component: _ba05daac,
    name: "topstreams"
  }, {
    path: "/game/:twitch?/:mixer?",
    component: _2d58a088,
    name: "game-twitch-mixer"
  }, {
    path: "/",
    component: _4aa2dcd6,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
