<template>
  <div>
      <h1>{{search.length}}편의 영화가 검색되었습니다.</h1>
    <b-card-group class="d-flex">
    <MovieCard v-for="movie in search" :movie="movie" :key="movie.movieId" class='col-3'/>
    </b-card-group>
  </div>
</template>

<script>
  import MovieCard from '@/components/MovieCard.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'SearchrMovieListView',
    components: {
      MovieCard,
    },
    data() {
    return {
      movieTitle: this.$route.params.movieTitle
    }
   },
    computed: {
      ...mapGetters(['search']),
    },
    methods: {
      ...mapActions(['searchMovie'])
    },
    created() {
      this.searchMovie(this.movieTitle)
    }
  }
</script>

<style>

</style>