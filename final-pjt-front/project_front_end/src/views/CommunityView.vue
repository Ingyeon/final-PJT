<template>
  <div>
    <h2 class="mx-auto mb-3 w-50 my-3 p-3 mb-2 bg-secondary bg-gradient text-white"> 전체 리뷰 </h2>
    <b-table hover :items="makeLists()" @row-clicked="rowClick">
    </b-table>
  </div>
</template>

<script>
import { mapGetters,mapActions } from 'vuex'
export default {
  name: 'CommunityView',
  props: {
    movieId : Number,
  },
  computed: {
    ...mapGetters(['reviews']),
    
  },
  methods: {
    ...mapActions(['fetchReviews']),
    // movie id에 맞는 리뷰 리스트
    makeLists(){
      const reviewlist = []
      for(let reviewitem of this.reviews ) { 
        {
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
      console.log(item)
      this.$router.push({
        path: `/community/${item.번호}`
      })
    }  
  },
  created(){
    this.fetchReviews()}
}
</script>

<style></style>
