<template>
  <div>
    <h2> Reviews </h2>
    <b-table hover :items="makeLists()" @row-clicked="rowClick">
    </b-table>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'ReviewList',
  props: {
    movieId : Number,
  },

  computed: {
    ...mapGetters(['reviews']),

  },
  methods: {
    makeLists(){
      const reviewlist = []
      for(let reviewitem of this.reviews ) {
        if(reviewitem.movie === this.movieId) {
            reviewlist.push({
              번호: reviewitem.pk,
              제목: reviewitem.title,
              작성자: reviewitem.user.username,
              좋아요: reviewitem.like_count,
              영화: reviewitem.movie_title,
              댓글: reviewitem.comment_count,
            })
        }
      }
      return reviewlist
    },
      rowClick(item){
      this.$router.push({
        path: `/community/${item.번호}`
      })
    }    
  },
}
</script>

<style>

</style>