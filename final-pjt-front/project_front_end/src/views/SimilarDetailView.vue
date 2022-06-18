<template>
  <div>
    <div>
      <h3 class="my-4"> 영화 세부 정보</h3>
      <b-card no-body class="overflow-hidden mx-auto" style="max-width: 540px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src= "`https://image.tmdb.org/t/p/w300${similardetail.poster_path}`" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body>
              <b-card-title> {{ similardetail.title }} </b-card-title>
              <b-card-text>
                개봉일 : {{ similardetail.release_date }}
              </b-card-text>
              <b-card-text>
                트렌드 점수 : {{ similardetail.popularity }}
              </b-card-text>
              <b-card-text>
                줄거리 : {{ similardetail.overview }}
              </b-card-text>
              <b-card-text>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>
    </div>

    <router-link :to="{ name: 'reviewCreate' }"> 새 리뷰 작성 </router-link>
    <hr>
    <h2 class='mx-auto mb-3 w-50 my-3 p-3 mb-2 bg-secondary bg-gradient text-white'>{{similardetail.title}}을 보신 분들이 같이 찾은 영화는 어떠세요?</h2>
    <smiliar-movie-list/>

  </div>
</template>

<script>
import SmiliarMovieList from '@/components/SmiliarMovieList.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'MovieDetailView',
  components: {
    SmiliarMovieList
  },
  data() {
    return {
      movieId: this.$route.params.movieId
    }
  },

  computed: {
    ...mapGetters(['similardetail','currentUser']),
    },
  methods: {
    ...mapActions([
      'fetchSimilarDetail',
    ]),
  },
  created(){
    this.fetchSimilarDetail(this.$route.params.movieId)
  }
}
</script>

<style>
.red {
  color: red;
}
</style>