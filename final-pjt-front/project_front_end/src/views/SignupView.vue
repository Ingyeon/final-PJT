<template>
  <div class="mx-auto my-3 p-3 border border-1 rounded" style="max-width:430px;">
    <h2>회원 가입</h2>

    <account-error-list v-if="authError" style="display: none"></account-error-list>
    <div style="max-width: 400px;" class="my-1">
      <b-form @submit.prevent="signup(credentials)" >
        <b-form-group id="username" label="아이디" label-for="아이디" class="my-1">
          <b-form-input id="username" v-model="credentials.username" type="text" placeholder="Enter Username" required />
        </b-form-group>

        <b-form-group id="password1" label="비밀번호" label-for="비밀번호" class="my-2">
          <b-form-input id="password1" v-model="credentials.password1" placeholder="Enter Password" type="password" required />
        </b-form-group>

        <b-form-group id="password2" label="비밀번호 확인" label-for="비밀번호 확인">
          <b-form-input id="password2" v-model="credentials.password2" placeholder="Check Password" type="password" required />
        </b-form-group>

        <b-button type="submit" variant="primary" class="mt-3">회원 가입</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>
