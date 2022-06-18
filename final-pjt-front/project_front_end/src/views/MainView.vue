<template>
  <div>
    <b-carousel
      id="carousel-fade"
      :interval="4000"
      controls
      fade
      indicators
      label-next = ''
      label-prev = ''
      img-width="1024"
      img-height="480"
      style="text-shadow: 0px 0px 2px #000"
    >

      <b-carousel-slide
        img-src="https://www.lunchbox-productions.com/wp-content/uploads/2021/10/Shows-Like-Carnival-Row-1024x480.jpg"
      ></b-carousel-slide>

      <b-carousel-slide img-src="https://www.lunchbox-productions.com/wp-content/uploads/2021/10/Movies-Like-Predestination-1024x480.jpg">
      </b-carousel-slide>

      <b-carousel-slide img-src="https://www.lunchbox-productions.com/wp-content/uploads/2021/10/Movies-Like-Miss-Congeniality-1024x480.jpg"></b-carousel-slide>

      <b-carousel-slide>
        <template #img>
          <img
            class="d-block img-fluid w-100"
            width="1024"
            height="480"
            src="https://maxxolife.com/wp-content/uploads/2021/06/new.jpg"
            alt="image slot"
          >
        </template>
      </b-carousel-slide>
    </b-carousel>


<!-- 케러셀 아래에 보여줄 영화 카드들 -->
  <h1 class=" mx-auto mb-3 w-50 my-3 p-3 mb-2 bg-secondary bg-gradient text-white">현재 상영중인 영화들</h1>
    <MovieList/>
  </div>
</template>

<script>
  import MovieList from '@/components/MovieList.vue'
  import { mapGetters,mapActions } from 'vuex'
  export default {
    components: {
      MovieList
    },
    computed: {
    ...mapGetters(['movies']),
  },
    methods: {
      ...mapActions(['fetchMovies']),
    },
    created() {
      this.fetchMovies()
    }
  }
</script>
