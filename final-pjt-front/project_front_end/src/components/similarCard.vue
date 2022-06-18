<template>
  <div>
    <router-link 
    @click.native="setLocalMovie(similardetail.movie_id)"
     :to="{ name: 'SimilarDetail', params: { movieId: similardetail.movie_id } }">
      <b-card
        img-alt="Image"
        img-top
        tag="article"
        style="max-width: 20rem;"
        class="mb-2"
        id="moviecard"
      >
      <b-card-img :src= "`https://image.tmdb.org/t/p/w300${similardetail.poster_path}`" id="card-img"/>
      <div id="bcardtitle">
        <b-card-title class="movietitle text-decoration-none"> {{ similardetail.title }} </b-card-title>
      </div>
      </b-card>
    </router-link>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  export default {
    name: 'similarCard',
    props: {
      similardetail: Object
    },
    
    methods: {
      ...mapActions(['fetchSimilarDetail','likeMovie']),
      setLocalMovie(movieid) {
        this.fetchSimilarDetail(movieid)
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

  h4.card-title.movietitle {
    line-height: 92px;
    vertical-align: middle;
    text-decoration: none;
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 1;
    -webkit-box-orient: vertical;
  }

  #moviecard {
    height : 518px;
    width : 318px;
    padding-bottom: 0px;
  }
</style>