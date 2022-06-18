<template>
  <div>
    <b-card-group class="d-flex justify-content-center">
    <MovieCard v-for="movie in genre" :movie="movie" :key="movie.movieId" class='mcs mx-2 row row-col-4'/>
    </b-card-group>
  </div>
</template>

<script>
  import MovieCard from '@/components/MovieCard.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'GenreMovieListView',
    components: {
      MovieCard,
    },
    data() {
    return {
      genreId: this.$route.params.genreId
    }
   },
    computed: {
      ...mapGetters(['genre']),
    },
    methods: {
      ...mapActions(['fetchGenre'])
    },
    created() {
      this.fetchGenre(this.genreId)
    }
  }
</script>

<style>
.mcs a {
  color: #2c3e50 ;
  text-decoration: none;
}
</style>