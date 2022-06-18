<template>
  <div>
    <!-- user 정보 -->
    <h3 class="mt-4 mb-2">{{profile.username}} 님의 프로필</h3>
    <div style="max-width:400px;" class="mx-auto d-flex justify-content-around">
      <!-- 팔로워 : {{ profile.followers.all|length }} / 팔로우: {{ profile.followings.all|length }} -->
      <span> 팔로워 : {{ followerCount }} </span>
      <span> 팔로우 : {{ followingCount }} </span>
    </div>
    <div v-if="profile.pk !== currentUser.pk">
      <!-- 팔로우 버튼 -->
      <b-button variant="dark" v-if="checkList" @click="follow(profile.pk)"> 언팔로우 </b-button>
      <b-button variant="outline-dark" v-else @click="follow(profile.pk)"> 팔로우 </b-button>
    </div>
    <hr>
    <!-- 좋아요한 영화 목록 -->
    <div style="max-width: 800px;" class="mx-auto my-4">
      <h4>{{profile.username}} 님이 좋아요한 영화</h4>
      <b-list-group>
        <!-- 영화 리스트로 -->
        <b-list-group-item>
          <router-link :to="{ name: 'MovieDetail', params: { movieId: like.movie_id } }">
          {{like.title}}
          </router-link>
        </b-list-group-item>
      </b-list-group>
    </div>
    
    <!-- 작성한 리뷰 목록-->
    <div style="max-width: 800px;" class="mx-auto my-5">
      <h4>{{profile.username}} 님이 작성한 리뷰</h4>
      <b-list-group>
        <b-list-group-item v-for="review in profile.reviews" :key="review.pk">
          <router-link :to="{ name: 'review', params: { reviewPk: review.pk } }">
            {{ review.title }}
          </router-link>
        </b-list-group-item>
      </b-list-group>
    </div>

  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile','currentUser','like']),
    checkList() {
      let flag = false
      const fol = this.profile.followers
      for(let i=0 ; i < fol.length; i++ ) {
        if (fol[i].pk === this.currentUser.pk) {
          flag = true
          break
        }
      }
      return flag
    },
    followerCount() {
      return this.profile.followers?.length
    },
    followingCount() {
      return this.profile.followings?.length
    }
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchCurrentUser','follow']),
  },
  created(){

    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
  
}
</script>

<style>
  a {
    text-decoration: none;
    color:#2c3e50 ;
  }
</style>