<template>
  <div>
    <h3 class="mt-3">영화 리뷰를 남겨주세요</h3>
    <ReviewForm :review="review" action="create" />
  </div>
</template>

<script>

import ReviewForm from '@/components/ReviewForm.vue'
export default {
  name: 'ReviewCreateView',
  components: 
    { ReviewForm },
  data() {
    return {
      review: {
        pk: null,
        title: '',
        content: '',
        rank : null,
        movie: null,
        movie_title: null,
      }
    }
  }

}
</script>

<style>

</style>

