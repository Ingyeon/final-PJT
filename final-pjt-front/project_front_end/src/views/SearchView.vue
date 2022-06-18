<template>
  <div>
    <p>{{movieTitle}}의 검색 결과</p>
  <SearchMovieList/>
  </div>

</template>

<script>
import SearchMovieList from '../components/SearchMovieList.vue'

export default {
  name: 'SearchView',
  components: {
    SearchMovieList
},
  data() {
    return {
      movieTitle: this.$route.params.movieTitle
    }
  },
}
</script>

<style>

</style>