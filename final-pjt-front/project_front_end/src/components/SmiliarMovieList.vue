<template>
  <div>
    <b-card-group class="d-flex justify-content-center">
    <similarCard v-for="similardetail in similar" :similardetail="similardetail" :key="similardetail.movieId"  class='mcs mx-2 row row-col-4'/>
    </b-card-group>
  </div>
</template>

<script>
  import similarCard from '@/components/similarCard.vue'
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'SimiliarMovieListView',
    components: {
      similarCard,
    },
    data() {
    return {
      movieId: this.$route.params.movieId
    }
   },
    computed: {
      ...mapGetters(['similar']),
    },
    methods: {
      ...mapActions(['fetchSimilar'])
    },
    created() {
      this.fetchSimilar(this.movieId)
    }
  }
</script>

<style>
.mcs a {
  color: #2c3e50 ;
  text-decoration: none;
}
</style>