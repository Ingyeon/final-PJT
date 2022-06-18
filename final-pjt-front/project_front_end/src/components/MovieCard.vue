<template>
  <div>
    <router-link 
    @click.native="setLocalMovie(movie.movie_id)"
     :to="{ name: 'MovieDetail', params: { movieId: movie.movie_id } }">
      <b-card
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
        id="moviecard"
      >
      <b-card-img :src= "`https://image.tmdb.org/t/p/w300${movie.poster_path}`" id="card-img"/>
      <div id="bcardtitle">
        <b-card-title class="movietitle "> {{ movie.title }} </b-card-title>
      </div>
      
      </b-card>
    </router-link>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'

  export default {
    name: 'MovieCard',

    props: {
      movie: Object
    },
    
    methods: {
      ...mapActions(['fetchMovie','likeMovie']),
      setLocalMovie(movieid) {
        this.fetchMovie(movieid)
      }
    }
  }
</script>

<style>
  #card-img {
    width : 286px;
    height: 410px;
  }
  #bcardtitle{
    height: 92px;
  }

  .movietitle {
    line-height: 84px;
    vertical-align: middle;

  }

  #moviecard {
    height : 518px;
    width : 318px;
    padding-bottom: 0px;

  }

  #bcardtitle h4 {
    text-decoration: none;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }
  
</style>