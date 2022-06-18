import Vue from 'vue'
import VueRouter from 'vue-router'

import LoginView from '@/views/LoginView.vue'
import LogoutView from '@/views/LogoutView.vue'
import SignupView from '@/views/SignupView.vue'
import ProfileView from '@/views/ProfileView.vue'

import CommunityView from '@/views/CommunityView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MovieGenreView from '@/views/MovieGenreView.vue'

import ReviewCreateView from '@/views/ReviewCreateView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewEditView from '@/views/ReviewEditView.vue'
import NotFound404 from '@/views/NotFound404.vue'
import MainView from '@/views/MainView.vue'
import SearchView from '@/views/SearchView.vue'
import SimilarDetailView from '@/views/SimilarDetailView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },

  {
    path: '/profile/:userPk/follow',
    name: 'follow',
    component: ProfileView 
  },

  {
    path: '/',  
    name: 'main',
    component: MainView
  },
  { path: '/search/:movieTitle',
    name: 'search',
    component: SearchView

  },
  { // 전체 리뷰 목록
    path: '/community',  
    name: 'community',
    component: CommunityView
  },
  {
    path: '/movies/detail/:movieId',  
    name: 'MovieDetail',
    component: MovieDetailView
  },
  {
    path: '/movies/similardetail/:movieId',
    name: 'SimilarDetail',
    component: SimilarDetailView
  },
  {
    path: '/movies/:genreId',  
    name: 'genreMovieList',
    component: MovieGenreView
  },
  {
    path: '/community/create',  
    name: 'reviewCreate',
    component: ReviewCreateView
  },
  { // 리뷰 디테일
    path: '/community/:reviewPk',  
    name: 'review',
    component: ReviewDetailView,
    props: true
  },
  {
    path: '/community/:reviewPk/edit',  
    name: 'reviewEdit',
    component: ReviewEditView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  scrollBehavior(){
    return {x:0 , y:0}
  },
  base: process.env.BASE_URL,
  routes
})

export default router