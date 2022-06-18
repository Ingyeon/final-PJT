<template>
  <ol class="list-group list-group-horizontal mx-auto">
      <li class="list-group-item py-1">
        <router-link class='fw-bold' :to="{ name: 'profile', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link>
      </li>
      <li class="list-group-item flex-fill" v-if="!isEditing">{{ payload.content }}</li>

      <li v-if="isEditing" >
        <input type="text" v-model="payload.content">
        <b-button @click="onUpdate"  variant="success" size="sm">Update</b-button> 
        <b-button @click="switchIsEditing" variant="danger" size="sm">Cancel</b-button>
      </li>

      <span v-if="currentUser.username === comment.user.username && !isEditing" class="px-1">
        <b-button @click="switchIsEditing" variant="success">Edit</b-button>
        <b-button @click="deleteComment(payload)" variant="danger">Delete</b-button>
      </span>
  </ol>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        reviewPk: this.comment.review,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>
</style>