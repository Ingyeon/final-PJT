<template>

  <div class="mx-auto my-3 p-3 border border-1 rounded" style="max-width:900px;">
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
              </div>
            </b-card-body>
          </b-col>
        </b-row>
      </b-card>

      <b-form @submit.prevent="onSubmit" class="py-3">
        <b-form-group id="title" label="제목 :" label-for="title" >
          <b-form-input id="title" v-model="newReview.title" type="text" placeholder="리뷰 제목을 입력하세요" required />
        </b-form-group>

        <b-form-group id="content" label="내용 :" label-for="content">
          <b-form-input id="content" v-model="newReview.content" placeholder="리뷰 내용을 입력하세요" type="text" required />
        </b-form-group>

        <b-form-group id="rank" label="평점 : " label-for="content">
          <b-form-input id="rank" v-model="newReview.rank" type="number" min="0" max="10" required />
        </b-form-group>

        <b-button type="submit" variant="primary" class="mt-3">등록</b-button>
      </b-form>

  </div>

    
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewForm',
  props: {
    review: Object,
    action: String,
  },
  
  computed: {
    ...mapGetters(['movie']),
  },

  data() {
    return {
      newReview: {
        title: this.review.title,
        content: this.review.content,
        rank: this.review.rank,
      }
    }
  },

  methods: {
    ...mapActions(['createReview','updateReview']),
    onSubmit() {
      if (this.action === 'create') {
        const payload = {
          movie: this.movie.movie_id,
          movie_title: this.movie.title,
          poster_path: this.movie.poster_path,
          ...this.newReview,
        }
        this.createReview(payload)
      } else if (this.action === 'update') {
        const payload = {
          movie: this.movie.movie_id,
          movie_title: this.movie.title,
          poster_path: this.movie.poster_path,
          pk: this.review.pk,
          ...this.newReview,
        }
        this.updateReview(payload)
      }
    }
  },

}
</script>

<style>

</style>