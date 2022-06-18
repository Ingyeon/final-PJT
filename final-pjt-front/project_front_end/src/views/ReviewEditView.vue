<template>
  <div>
    <h2 class="my-2">리뷰 수정</h2>
    <ReviewForm v-if="isReview" :review="review" action="update"/>
  </div>
  
</template>

<script>

import ReviewForm from '@/components/ReviewForm.vue'
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ReviewEditView',
  components: {
    ReviewForm
  },
  computed: {
    ...mapGetters(['review','isReview',])
  },
  methods: {
    ...mapActions(['fetchReview'])
  },
}
</script>

<style>

</style>