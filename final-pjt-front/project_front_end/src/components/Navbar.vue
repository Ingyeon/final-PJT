<template>
<div class="d-block">
  <b-navbar type="dark" variant="dark">
    <b-navbar-nav>  
    <b-navbar-brand class="fw-bold">
      <img src="https://placekitten.com/g/30/30" class="d-inline-block align-top" alt="Kitten">
      Movie in Revue
    </b-navbar-brand>
      <!-- navbar 링크 목록, b-navbar-nav 내부에 값 넣기 -->
        <b-nav-item :to="{ name: 'main' }">Home</b-nav-item>
        <!-- 드롭다운 -->
    <b-nav-item-dropdown text="Genre" right>
      
      <b-dropdown-item :to="{ name: 'genreMovieList', params: { genreId: 28 } }">액션</b-dropdown-item>
      <b-dropdown-item :to="{ name: 'genreMovieList', params: { genreId: 99 } }">다큐맨터리</b-dropdown-item>
      <b-dropdown-item :to="{ name: 'genreMovieList', params: { genreId: 16 } }" >애니메이션</b-dropdown-item>
      <b-dropdown-item :to="{ name: 'genreMovieList', params: { genreId: 27 } }">공포</b-dropdown-item>
      <b-dropdown-item :to="{ name: 'genreMovieList', params: { genreId: 10749 } }">로맨스</b-dropdown-item>
    </b-nav-item-dropdown>
    <b-nav-item :to="{ name: 'community' }">Community</b-nav-item>
          </b-navbar-nav>

      <!-- 검색창 -->
    <b-container fluid is-nav class="d-flex justify-content-end">
    <b-navbar-nav class="d-flex">
      <form class="d-flex">
        <b-form-input size="sm" class="mr-sm-2 my-2" placeholder="Search" v-model="keyword" @keyup.enter="searchResult(keyword)"></b-form-input>
        <b-button size="sm" class="my-2 mr-sm-0 mx-2" type="submit" @click="searchResult(keyword)">Search</b-button>
      </form>
          <!-- if 분기- 로그인 여부 -->
          <b-nav-item-dropdown right v-if="!isLoggedIn" class="ml-auto">
          <template #button-content>
            <em>guest</em>
          </template>
          <b-dropdown-item :to="{ name: 'login' }">로그인</b-dropdown-item>
          <b-dropdown-item :to="{ name: 'signup' }">회원 가입</b-dropdown-item>
        </b-nav-item-dropdown>
        <!-- 로그인 아닐 경우 -->
        <b-nav-item-dropdown right v-if="isLoggedIn" class="ml-auto">
          <template #button-content>
            <em class="text-align-center">{{username}}</em>
          </template>
          <b-dropdown-item :to="{ name:'profile', params: { username: username }}">프로필</b-dropdown-item>
          <b-dropdown-item :to="{ name: 'logout' }">로그아웃</b-dropdown-item>
        </b-nav-item-dropdown>

      </b-navbar-nav>
      </b-container>
  </b-navbar>
</div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
  name: 'NavBar',
  data(){
    return {
      keyword: ''
    }
  },
  computed: {
    ...mapGetters(['isLoggedIn','currentUser']),
    username(){
      return this.currentUser.username ? this.currentUser.username : 'guest'
    },
  },
  methods: {
    searchResult(keyword){
      if (keyword != ''){
        this.$router.push({
          name: "search",
          params: {
            movieTitle: this.keyword
          }
        })
      this.keyword = ''
      }
      else {alert('검색어를 입력해주세요!')}
    }
  }
}
</script>

<style>
</style>


