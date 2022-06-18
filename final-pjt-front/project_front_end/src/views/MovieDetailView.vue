<template>
  <div>
    <div>
      <h3 class="my-4"> 영화 세부 정보</h3>
      <b-card no-body class="overflow-hidden mx-auto" style="max-width: 900px;">
        <b-row no-gutters>
          <b-col md="6" class="detail-part">
            <b-card-img :src= "`https://image.tmdb.org/t/p/w300${movie.poster_path}`" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6" class="detail-part pl-0">
            <b-card-body>
              <b-card-title class="title my-3"> {{ movie.title }} </b-card-title>
              <div class="d-flex flex-column justify-content-around">
                <b-card-text>
                  개봉일 : {{ movie.release_date }}
                </b-card-text>
                <b-card-text>
                  트렌드 점수 : {{ movie.popularity }}
                </b-card-text>
                <b-card-text>
                  줄거리 : <br>
                  {{ movie.overview }}
                </b-card-text>
                <b-card-text>
                      좋아요:
                      <button @click="makelike()" class="like-button">
                      <font-awesome-icon v-if="flag==false" icon="fa-regular fa-heart"/>
                      <font-awesome-icon v-else icon="fa-solid fa-heart" class=red />
                      </button>
                </b-card-text>
                    <router-link :to="{ name: 'reviewCreate' }" class="btn btn-primary my-2" > 새 리뷰 작성 </router-link>
              </div>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>

    <ReviewList :movieId="movie.movie_id"/>
    <hr>
    <h2 class='mx-auto mb-3 w-50 my-3 p-3 mb-2 bg-secondary bg-gradient text-white'>{{movie.title}}을 보신 분들이 같이 찾은 영화는 어떠세요?</h2>
    <smiliar-movie-list />

  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'
import SmiliarMovieList from '@/components/SmiliarMovieList.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'MovieDetailView',
  components: {
    SmiliarMovieList,
    ReviewList
  },
  data() {
    return {
      movieId: this.$route.params.movieId,
      flag: {}
    }
  },

  computed: {
    ...mapGetters(['movie','currentUser','like']),
  },
  methods: {
    ...mapActions([
      'likeMovie',
    ]),
    makelike(){
      this.likeMovie(this.movieId)
      if (this.flag == false){
        return this.flag = true
      }
      else {
        return this.flag = false
      }
    },

      likeCheck(){
        if (this.like.movie_Id == this.movieId) {
          return this.flag = true
        }
        else if (this.like.movie_Id != this.movieId)
        {return this.flag = false}
    },
  },
  created(){
    this.likeCheck()
  }
}
</script>

<style>
.red {
  color: red;
}
.like-button {
  border:0;
  outline:0;
  background-color:white;
}
.card-text {
  text-align:start ;
}
.card-img {
  height: 100%;
}
#info {
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

</style>