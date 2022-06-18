<template>
  <div>
    <h3 class="my-4"> 상세 리뷰 </h3>
    <div style="max-width: 900px;" class="mx-auto">
      <b-card no-body class="overflow-hidden mx-auto" style="max-width: 900px;">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img :src= "`https://image.tmdb.org/t/p/w300${review.poster_path}`" alt="Image" class="rounded-0"></b-card-img>
          </b-col>
          <b-col md="6">
            <b-card-body>
              <b-card-title class="title my-3"> {{ review.title }} </b-card-title>
              <b-card-text>
                작성자 : <router-link :to="{name: 'profile', params: {username:review.user.username}}">{{review.user.username}}</router-link>
              </b-card-text>
              <b-card-text>
                평점 : {{ review.rank }}
              </b-card-text>
              <b-card-text>
                {{ review.content }}
              </b-card-text>

            </b-card-body>
            <b-card-footer id="sbuttons">
              <!-- review Edit/Delete UI -->
              <span v-if="isAuthor">
                <router-link :to="{ name: 'reviewEdit', params: { reviewPk } }">
                  <b-button variant="success" >Edit</b-button>
                </router-link>
                 &nbsp;
                <b-button variant="danger" @click="deleteReview(reviewPk)">Delete</b-button>
              </span>
              <!-- review Like UI -->
              <span>
                <b-button variant="secondary" @click="likeReview(reviewPk)"> Likeit: {{ likeCount }}</b-button>
              </span>

            </b-card-footer>
          </b-col>
        </b-row>
      </b-card>
    <hr />
    <!-- Comment UI -->
    <comment-list :comments="review.comments"></comment-list>
    </div>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'



  export default {
    name: 'reviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewPk: this.$route.params.reviewPk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      likeCount() {
        return this.review.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchReview',
        'likeReview',
        'deleteReview',
        'fetchReviews'
      ])
    },
    created() {
      this.fetchReview(this.reviewPk)
      this.fetchReviews()
    },
  }
</script>

<style>
  #sbuttons {
    background-color: white;
    display: flex;
    justify-content: space-evenly;
  }
</style>
