<template>
  <div>
  <h4> 댓글 목록</h4>
      <CommentListItem
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk" />    <CommentListForm/>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'

export default {
  name: 'CommentList',
  components: {
    CommentListForm,
    CommentListItem
  },
  props: {
    comments: Array
  },
}
</script>

<style>
</style>