<template>
  <div class="d-flex comment-list-form mx-auto">
    <b-input-group class="mt-3">
    <b-input-group-text class="height">댓글</b-input-group-text>
    <b-form-textarea @submit.prevent="onSubmit" id="textarea" v-model="content" placeholder="댓글을 달아주세요" required />
    <b-input-group-append>
      <b-button variant="outline-primary" class="height mx-1"  @click="onSubmit">작성하기</b-button>
    </b-input-group-append>
  </b-input-group>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'CommentListForm',
  data() {
    return {
      name: "댓글",
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ reviewPk: this.review.pk, content: this.content})
      this.content = ''
    }
  }
}
</script>


<style>
.comment-list-form {
  margin-bottom: 1em;
  padding: 1rem;
}
.height {
  height: 70px;
}
</style>