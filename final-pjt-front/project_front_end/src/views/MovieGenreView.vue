<template>
  <div>
    <h3 class="mt-2 mx-auto mb-3 w-50 my-3 p-3 mb-2 bg-secondary bg-gradient text-white">{{genre_name}} 장르의 영화 목록입니다.</h3>
  <GenreMovieList/>
  </div>
</template>

<script>
import GenreMovieList from '@/components/GenreMovieList.vue'
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'MovieGenreView',
  components: {
    GenreMovieList,
},
  data() {
    return {
      genreId: this.$route.params.genreId,
      genre_name: ''
    }
  },

  computed: {
    ...mapGetters(['genre']),
  },
  methods: {
    ...mapActions([
      'fetchGenre'
    ]),
  findGenre(){
    if (this.genreId == 28){
      return this.genre_name = '액션'
    }
    else if(this.genreId == 99){
      return this.genre_name = '다큐맨터리'
    }
    else if(this.genreId == 16){
      return this.genre_name = '애니메이션'
    }
    else if(this.genreId == 27){
      return this.genre_name = '공포'
    }
    else if(this.genreId == 10749){
      return this.genre_name = '로맨스'
    }
  },},
  created(){
    this.fetchGenre(this.genreId)
    this.findGenre()
  },
}
</script>

<style>

</style>